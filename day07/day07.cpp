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

bool calc(int64_t inter, const int64_t& result, deque<int64_t> numbers, char oper) {
    // optimization
    if (inter > result) {
        return false;
    }
    if (numbers.empty()) {
        if (inter == result) {
            return true;
        }
        else return false;
    }
    auto nr = numbers.front();
    numbers.pop_front();

    if (oper == '+') {
        auto inter1 = inter + nr;
        return (calc(inter1, result, numbers, '+') || calc(inter1, result, numbers, '*'));
    } else {
        auto inter2 = inter * nr;
        return (calc(inter2, result, numbers, '+') || calc(inter2, result, numbers, '*'));
    }
}

bool calc2(int64_t inter, const int64_t& result, deque<int64_t> numbers, char oper) {
    // optimization
    if (inter > result) {
        return false;
    }
    if (numbers.empty()) {
        if (inter == result) {
            return true;
        }
        else return false;
    }
    auto nr = numbers.front();
    numbers.pop_front();

    if (oper == '+') {
        auto inter1 = inter + nr;
        return (
            calc2(inter1, result, numbers, '+') || 
            calc2(inter1, result, numbers, '*') || 
            calc2(inter1, result, numbers, '|') );
    } else if (oper == '*') {
        auto inter2 = inter * nr;
        return (
            calc2(inter2, result, numbers, '+') || 
            calc2(inter2, result, numbers, '*') ||
            calc2(inter2, result, numbers, '|') );
    } else {
        auto inter3 = stoll(to_string(inter) + to_string(nr));
        return (
            calc2(inter3, result, numbers, '+') || 
            calc2(inter3, result, numbers, '*') ||
            calc2(inter3, result, numbers, '|') );
    }
}


int64_t d07pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int64_t result = 0;

    for (auto line : lines) {
        auto res_nrs = split(line, ": ");
        auto res = stoll(res_nrs[0]);
        auto nrs = convert_to_int64(split(res_nrs[1], " "));

        deque<int64_t> numbers(nrs.begin(), nrs.end());
        int64_t inter = 0;

        if (calc(inter, res, numbers, '+')) {
            result += res;
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

        deque<int64_t> numbers(nrs.begin(), nrs.end());
        int64_t inter = 0;

        if (calc2(inter, res, numbers, '+')) {
            result += res;
        }

    }
    return result;
}