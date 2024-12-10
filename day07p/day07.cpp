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

bool calc_state(int32_t state, const int64_t& result, vector<int64_t> numbers) {
    int64_t intermediate = numbers.front();
    if (intermediate >= result) return false;

    for (auto it = numbers.cbegin() + 1; it != numbers.cend(); it++) {
        if (intermediate > result) {
            return false;
        }

        auto op = state & 1;
        if (op) {
            intermediate += *it;
        } else {
            intermediate *= *it;
        }
        state = state>>1;
    }

    return intermediate == result;
}

bool calc_state2(int32_t state, const int64_t& result, vector<int64_t> numbers) {
    int64_t intermediate = numbers.front();
    if (intermediate >= result) return false;

    for (auto it = numbers.cbegin() + 1; it != numbers.cend(); it++) {
        if (intermediate > result) {
            return false;
        }

        auto op = state % 3;
        if (op==0) {
            intermediate += *it;
        } else if (op==1) {
            intermediate *= *it;
        } else{
            intermediate = stoll(to_string(intermediate) + to_string(*it));
        }
        state = state / 3;
    }

    return intermediate == result;
}

int64_t d07pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int64_t result = 0;

    for (auto line : lines) {
        auto res_nrs = split(line, ": ");
        auto res = stoll(res_nrs[0]);
        auto nrs = convert_to_int64(split(res_nrs[1], " "));

        int8_t number_of_instructions = nrs.size() - 1;
        int32_t max_state = ipow(2, number_of_instructions);

        for (int i = 0; i < max_state; i++) {
            if (calc_state(i, res, nrs)) {
                result += res;
                break;
            }
        }
    }
    return result;
}

int64_t d07pt2(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int64_t result = 0;

    for (auto line : lines) {
        auto res_nrs = split(line, ": ");
        auto res = stoll(res_nrs[0]);
        auto nrs = convert_to_int64(split(res_nrs[1], " "));

        int8_t number_of_instructions = nrs.size() - 1;
        int32_t max_state = ipow(3, number_of_instructions);
        
        for (int i = 0; i < max_state; i++) {
            if (calc_state2(i, res, nrs)) {
                result += res;
                break;
            }
        }
    }
    return result;
}