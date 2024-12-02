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

#include "util.hpp"
#include "gfx/timsort.hpp"

using namespace std;


int d01pt1(const filesystem::path& file_path) {
    //cout << endl << "Day 01 - Pt1: " << file_path.filename() << endl;
    const auto lines = read_lines(file_path);
    int result = 0;

    vector<int> left;
    vector<int> right;

    for (auto line : lines) {
        auto l_r = split(line, "   ");
        left.push_back(stoi(l_r[0]));
        right.push_back(stoi(l_r[1]));
    }

    gfx::timsort(left.begin(), left.end());
    gfx::timsort(right.begin(), right.end());

    for (int i = 0; i < left.size(); i++) {
        result += abs(left[i] - right[i]);
    }

    return result;
}

int d01pt2(const filesystem::path& file_path) {
    //cout << endl << "Day 01 - Pt2: " << file_path.filename() << endl;
    auto lines = read_lines(file_path);
    int result = 0;

    vector<int> left;
    vector<int> right;

    for (auto line : lines) {
        auto l_r = split(line, "   ");
        left.push_back(stoi(l_r[0]));
        right.push_back(stoi(l_r[1]));
    }

    for (auto l : left) {
        for (auto r : right) {
            if (l == r) {
                result += l;
            }
        }
    }

    return result;
}
