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

#include "util.hpp"

using namespace std;


int64_t d01pt1(const filesystem::path& file_path) {
    cout << endl << "Day 01 - Pt1: " << file_path.filename() << endl;
    auto lines = read_lines(file_path);
    int result = 0;

    for (auto line : lines) {
        result++;
    }
    return result;
}

int64_t d01pt2(const filesystem::path& file_path) {
    cout << endl << "Day 01 - Pt2: " << file_path.filename() << endl;
    auto lines = read_lines(file_path);
    int result = 0;

    for (auto line : lines) {
        result++;
    }
    return result;
}
