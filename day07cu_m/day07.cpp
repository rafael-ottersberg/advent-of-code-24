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
    const std::vector<std::vector<int64_t>>& numbers,
    const std::vector<int64_t>& results, 
    const std::vector<int32_t>& number_of_combinations,
    int32_t total_combinations, int32_t part);

int64_t d07pt1cu_m(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);

    vector<vector<int64_t>> numbers;
    vector<int64_t> results;
    vector<int32_t> number_of_combinations;
    int32_t total_combinations = 0;
    for (auto line : lines) {
        auto res_nrs = split(line, ": ");
        auto res = stoll(res_nrs[0]);
        auto nrs = convert_to_int64(split(res_nrs[1], " "));

        int8_t number_of_instructions = nrs.size() - 1;
        int32_t combinations = ipow(2, number_of_instructions);
        number_of_combinations.push_back(combinations);
        total_combinations += combinations;
        numbers.push_back(nrs);
        results.push_back(res);
    }

    return calc_states(numbers, results, number_of_combinations, total_combinations, 1);
}

int64_t d07pt2cu_m(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);

    vector<vector<int64_t>> numbers;
    vector<int64_t> results;
    vector<int32_t> number_of_combinations;
    int32_t total_combinations;
    for (auto line : lines) {
        auto res_nrs = split(line, ": ");
        auto res = stoll(res_nrs[0]);
        auto nrs = convert_to_int64(split(res_nrs[1], " "));

        int8_t number_of_instructions = nrs.size() - 1;
        int32_t combinations = ipow(3, number_of_instructions);
        number_of_combinations.push_back(combinations);
        total_combinations += combinations;
        numbers.push_back(nrs);
        results.push_back(res);
    }

    return calc_states(numbers, results, number_of_combinations, total_combinations, 2);
}
