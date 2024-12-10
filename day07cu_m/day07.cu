#include <vector>

#include <thrust/device_vector.h>
#include <thrust/host_vector.h>
#include <thrust/sort.h>
#include <thrust/unique.h>
#include <thrust/remove.h>

__device__ inline void int_to_string(int64_t value, char* str) {
    char* ptr = str;
    if (value == 0) {
        *ptr++ = '0';
    } else {
        if (value < 0) {
            *ptr++ = '-';
            value = -value;
        }
        char* start = ptr;
        while (value) {
            *ptr++ = '0' + (value % 10);
            value /= 10;
        }
        *ptr = '\0';
        // Reverse the string
        char* end = ptr - 1;
        while (start < end) {
            char temp = *start;
            *start++ = *end;
            *end-- = temp;
        }
    }
    *ptr = '\0';
}

__device__ inline int64_t string_to_int(const char* str) {
    int64_t result = 0;
    while (*str) {
        result = result * 10 + (*str - '0');
        str++;
    }
    return result;
}

__device__ inline size_t cu_strlen(const char* str) {
    size_t len = 0;
    while (*str++) {
        len++;
    }
    return len;
}

__device__ inline int64_t concatenate_integers(int64_t a, int64_t b) {
    char str[64] = {0}; // Initialize to ensure it's empty
    int_to_string(a, str);
    int_to_string(b, str + cu_strlen(str)); // Append b to the end of the string representation of a
    return string_to_int(str);
}

struct is_zero
{
    __host__ __device__
    bool operator()(const int64_t x) const
    {
        return x == 0;
    }
};


__global__ void calc_state_kernel(
    int64_t* numbers, int32_t numbers_size, int64_t result, int32_t combinations, int64_t* ret, int32_t return_offset) {
    
    int32_t idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= combinations) return;

    int32_t state = idx;
    int32_t return_idx = return_offset + idx;
    int64_t intermediate = numbers[0];
    for (auto i = 1; i < numbers_size; i++) {
        int64_t number = numbers[i];

        if (intermediate > result) {
            ret[return_idx] = 0;
            return;
        }

        auto op = state & 1;
        if (op) {
            intermediate += number;
        } else {
            intermediate *= number;
        }
        state = state>>1;
    }
    if (intermediate == result) {
        ret[return_idx] = result;
    } else {
        ret[return_idx] = 0;
    }
    return;
}

__global__ void calc_state_kernel2(
    int64_t* numbers, int32_t numbers_size, int64_t result, int32_t combinations, int64_t* ret, int32_t return_offset) {
    
    int32_t idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= combinations) return;

    int32_t state = idx;
    int32_t return_idx = return_offset + idx;
    int64_t intermediate = numbers[0];
    for (auto i = 1; i < numbers_size; i++) {
        int64_t number = numbers[i];

        if (intermediate > result) {
            ret[return_idx] = 0;
            return;
        }

        auto op = state % 3;
        if (op==0) {
            intermediate += number;
        } else if (op==1) {
            intermediate *= number;
        } else {
            intermediate = concatenate_integers(intermediate, number);
        }
        state = state / 3;
    }
    if (intermediate == result) {
        ret[return_idx] = result;
    } else {
        ret[return_idx] = 0;
    }
    return;
}

int64_t calc_states(
    const std::vector<std::vector<int64_t>>& numbers, 
    const std::vector<int64_t>& results,
    const std::vector<int32_t>& number_of_combinations,
    int32_t total_combinations, int32_t part) {
    
    // prepare return vector
    thrust::device_vector<int64_t> d_return(total_combinations);
    int64_t* d_return_ptr = thrust::raw_pointer_cast(d_return.data());

    int32_t return_idx_offset = 0;
    for (size_t i = 0; i < numbers.size(); i++) {
        // Copy data to device
        thrust::device_vector<int64_t> d_numbers(numbers[i]);
        int64_t* d_numbers_ptr = thrust::raw_pointer_cast(d_numbers.data());
        int32_t numbers_size = numbers[i].size();

        int64_t result = results[i];
        int32_t combinations = number_of_combinations[i];

        int block_size = 1024;
        int grid_size = (combinations + block_size - 1) / block_size;
        if (part == 1) {
            calc_state_kernel<<<grid_size, block_size>>>(
                d_numbers_ptr, numbers_size, result, combinations, d_return_ptr, return_idx_offset);
        } else {
            calc_state_kernel2<<<grid_size, block_size>>>(
                d_numbers_ptr, numbers_size, result, combinations, d_return_ptr, return_idx_offset);
        }
        return_idx_offset += combinations;
    }
    cudaDeviceSynchronize();
    
    // Remove zeros
    auto end = thrust::remove_if(d_return.begin(), d_return.end(), is_zero());
    d_return.erase(end, d_return.end());
    // Remove duplicates
    end = thrust::unique(d_return.begin(), d_return.end());
    d_return.erase(end, d_return.end());
    // Sum
    int64_t sum = thrust::reduce(d_return.begin(), d_return.end(), int64_t(0));

    return sum;
}