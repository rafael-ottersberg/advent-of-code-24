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

int64_t d24pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    for (auto line : lines) {
        result++;
    }
    return result;
}

int64_t d24pt2(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    for (auto line : lines) {
        result++;
    }
    return result;
}