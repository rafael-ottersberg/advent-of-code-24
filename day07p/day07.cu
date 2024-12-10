#include <vector>

#include <thrust/device_vector.h>
#include <thrust/host_vector.h>
#include <thrust/sort.h>
#include <thrust/unique.h>
#include <thrust/remove.h>

__device__ void int_to_string(int64_t value, char* str) {
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

__device__ int64_t string_to_int(const char* str) {
    int64_t result = 0;
    while (*str) {
        result = result * 10 + (*str - '0');
        str++;
    }
    return result;
}

__device__ size_t cu_strlen(const char* str) {
    size_t len = 0;
    while (*str++) {
        len++;
    }
    return len;
}

__device__ int64_t concatenate_integers(int64_t a, int64_t b) {
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
    int32_t total_combinations, 
    int64_t* numbers, int32_t* cum_number_lengths,
    int64_t* results, int32_t* cum_combinations,
    int64_t* ret) {
    int32_t idx_combination = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx_combination >= total_combinations) {
        return;
    }

    int32_t idx_line = 0;
    while(true) {
        if (cum_combinations[idx_line] > idx_combination) {
            break;
        }
        idx_line++;
    }

    int32_t offset_idx_numbers = 0;
    int32_t offset_idx_combinations = 0;

    if (idx_line > 0) {
        offset_idx_numbers = cum_number_lengths[idx_line - 1];
        offset_idx_combinations = cum_combinations[idx_line - 1];
    }

    auto result = results[idx_line];

    int32_t state = idx_combination - offset_idx_combinations;
    int32_t in = offset_idx_numbers;
    int64_t intermediate = numbers[in];
    for (in = in + 1; in < cum_number_lengths[idx_line]; in++) {
        int64_t number = numbers[in];

        if (intermediate > result) {
            ret[idx_combination] = 0;
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
        ret[idx_combination] = result;
    } else {
        ret[idx_combination] = 0;
    }
    return;
}

__global__ void calc_state_kernel2(
    int64_t total_combinations, 
    int64_t* numbers, int32_t* cum_number_lengths,
    int64_t* results, int32_t* cum_combinations,
    int64_t* ret) {
    int32_t idx_combination = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx_combination >= total_combinations) {
        return;
    }

    int32_t idx_line = 0;
    while(true) {
        if (cum_combinations[idx_line] > idx_combination) {
            break;
        }
        idx_line++;
    }

    int32_t offset_idx_numbers = 0;
    int32_t offset_idx_combinations = 0;

    if (idx_line > 0) {
        offset_idx_numbers = cum_number_lengths[idx_line - 1];
        offset_idx_combinations = cum_combinations[idx_line - 1];
    }

    auto result = results[idx_line];

    int32_t state = idx_combination - offset_idx_combinations;
    int32_t in = offset_idx_numbers;
    int64_t intermediate = numbers[in];
    for (in = in + 1; in < cum_number_lengths[idx_line]; in++) {
        int64_t number = numbers[in];

        if (intermediate > result) {
            ret[idx_combination] = 0;
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
        ret[idx_combination] = result;
    } else {
        ret[idx_combination] = 0;
    }
    return;
}

template<typename T>
T* copy_vector_to_gpu(const std::vector<T>& vec) {
    thrust::device_vector<T> d_vec(vec);
    return thrust::raw_pointer_cast(d_vec.data());
}

int64_t calc_states(
    const std::vector<int64_t>& numbers, std::vector<int32_t>& number_lengths, 
    const std::vector<int64_t>& results, std::vector<int32_t>& number_of_combinations,
    int part) {
    
    auto d_numbers_ptr = copy_vector_to_gpu(numbers);

    // cumulative sum of numbers length to get number offset from line idx
    thrust::inclusive_scan(number_lengths.begin(), number_lengths.end(), number_lengths.begin());
    thrust::device_vector<int32_t> d_number_lengths(number_lengths);
    int32_t* d_number_lengths_ptr = thrust::raw_pointer_cast(d_number_lengths.data());
    
    // cumulative sum of number of combinations to get line idx from combination idx
    thrust::inclusive_scan(number_of_combinations.begin(), number_of_combinations.end(), number_of_combinations.begin());
    thrust::device_vector<int32_t> d_combinations(number_of_combinations);
    int32_t* d_combinations_ptr = thrust::raw_pointer_cast(d_combinations.data());


    thrust::device_vector<int64_t> d_results(results);
    int64_t* d_results_ptr = thrust::raw_pointer_cast(d_results.data());

    // get the number of threads launched
    int64_t total_combinations = number_of_combinations.back();

    // prepare return vector
    thrust::device_vector<int64_t> d_ret(total_combinations);
    int64_t* d_ret_ptr = thrust::raw_pointer_cast(d_ret.data());

    int block_size = 1024;
    int grid_size = (total_combinations + block_size - 1) / block_size;
    if (part == 1) {
        calc_state_kernel<<<grid_size, block_size>>>(total_combinations, d_numbers_ptr, d_number_lengths_ptr, d_results_ptr, d_combinations_ptr, d_ret_ptr);
    } else {
        calc_state_kernel2<<<grid_size, block_size>>>(total_combinations, d_numbers_ptr, d_number_lengths_ptr, d_results_ptr, d_combinations_ptr, d_ret_ptr);
    }
    cudaDeviceSynchronize();
    
    // Remove zeros
    auto end = thrust::remove_if(d_ret.begin(), d_ret.end(), is_zero());
    d_ret.erase(end, d_ret.end());
    // Remove duplicates
    end = thrust::unique(d_ret.begin(), d_ret.end());
    d_ret.erase(end, d_ret.end());

    int64_t sum = thrust::reduce(d_ret.begin(), d_ret.end(), int64_t(0));

    return sum;
}