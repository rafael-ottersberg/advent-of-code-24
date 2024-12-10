#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <set>
#include <functional>
#include <algorithm>
#include <filesystem>
#include <numeric>
#include <cstdint>
#include <regex>
#include <deque>

#include "util.hpp"

using namespace std;

int64_t calc_states(
    const std::vector<int64_t>& numbers, std::vector<int32_t>& cum_number_lengths, 
    const std::vector<int64_t>& results, std::vector<int32_t>& cum_number_of_combinations,
    int32_t part);

int64_t d07pt1cu(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);

    vector<int64_t> numbers;
    vector<int32_t> cum_number_lengths;
    vector<int64_t> results;
    vector<int32_t> cum_number_of_combinations;
    
    int32_t number_of_combinations_sum = 0;
    int32_t number_lengths_sum = 0;
    for (auto line : lines) {
        auto res_nrs = split(line, ": ");
        auto res = stoll(res_nrs[0]);
        auto nrs = convert_to_int64(split(res_nrs[1], " "));

        int8_t number_of_instructions = nrs.size() - 1;
        number_of_combinations_sum += ipow(2, number_of_instructions);
        numbers.insert(numbers.end(), nrs.begin(), nrs.end());
        number_lengths_sum += nrs.size();
        cum_number_lengths.push_back(number_lengths_sum);
        results.push_back(res);
        cum_number_of_combinations.push_back(number_of_combinations_sum);
    }

    return calc_states(numbers, cum_number_lengths, results, cum_number_of_combinations, 1);
}

int64_t d07pt2cu(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);

    vector<int64_t> numbers;
    vector<int32_t> cum_number_lengths;
    vector<int64_t> results;
    vector<int32_t> cum_number_of_combinations;
    
    int32_t number_of_combinations_sum = 0;
    int32_t number_lengths_sum = 0;
    for (auto line : lines) {
        auto res_nrs = split(line, ": ");
        auto res = stoll(res_nrs[0]);
        auto nrs = convert_to_int64(split(res_nrs[1], " "));

        int8_t number_of_instructions = nrs.size() - 1;
        number_of_combinations_sum += ipow(3, number_of_instructions);
        numbers.insert(numbers.end(), nrs.begin(), nrs.end());
        number_lengths_sum += nrs.size();
        cum_number_lengths.push_back(number_lengths_sum);
        results.push_back(res);
        cum_number_of_combinations.push_back(number_of_combinations_sum);
    }

    return calc_states(numbers, cum_number_lengths, results, cum_number_of_combinations, 2);
}
