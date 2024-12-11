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

#include "util.hpp"

using namespace std;

int64_t solve_number(int64_t number, int blinks, unordered_map<pair<int64_t, int>, int64_t, pair_hash>& cache) {
    if (blinks == 0) return 1;

    auto p = make_pair(number, blinks);
    if (cache.contains(p)) {
        return cache[p];
    }

    int64_t result;
    --blinks;
    if (number == 0) {
        result = solve_number(1, blinks, cache);
        cache[p] = result;
        return result;
    } 
    string n_str = to_string(number);
    int l = n_str.size();
    if (l % 2 == 0) {
        int l_2 = l / 2;
        int64_t n_left = stoll(n_str.substr(0, l_2));
        int64_t n_right = stoll(n_str.substr(l_2, l_2));
        result = solve_number(n_left, blinks, cache) + solve_number(n_right, blinks, cache);
        cache[p] = result;
        return result;
    }
    result = solve_number(number * 2024, blinks, cache);
    cache[p] = result;
    return result;
} 

int64_t d11pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int64_t result = 0;

    auto numbers = convert_to_int32(split(lines[0], " "));

    unordered_map<pair<int64_t, int>, int64_t, pair_hash> cache;
    for (auto n : numbers) {
        result += solve_number(n, 25, cache);
    }
    return result;
}

int64_t d11pt2(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int64_t result = 0;

    auto numbers = convert_to_int32(split(lines[0], " "));

    unordered_map<pair<int64_t, int>, int64_t, pair_hash> cache;
    for (auto n : numbers) {
        result += solve_number(n, 75, cache);
    }
    return result;
}