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

bool horizontal_substring(const vector<string>& lines, string& sub, const int32_t& i, const int32_t& j) {
    sub = "";
    if (j + 3 < static_cast<int32_t>(lines[0].size())) {
        for (int jj = j; jj < j + 4; jj++) {
            sub += lines[i][jj];
        }
        return true;
    } else {
        return false;
    }
}

bool vertical_substring(const vector<string>& lines, string& sub, const int32_t& i, const int32_t& j) {
    sub = "";
    if (i + 3 < static_cast<int32_t>(lines.size())) {
        for (int ii = i; ii < i + 4; ii++) {
            sub += lines[ii][j];
        }
        return true;
    } else {
        return false;
    }
}

bool d1_substring(const vector<string>& lines, string& sub, const int32_t& i, const int32_t& j) {
    sub = "";
    if ((i + 3 < static_cast<int32_t>(lines.size())) && (j + 3 < static_cast<int32_t>(lines[0].size()))) {
        for (int x = 0; x < 4; x++) {
            sub += lines[i+x][j+x];
        }
        return true;
    } else {
        return false;
    }
}

bool subcross(const vector<string>& lines, string& sub1, string& sub2, const int32_t& i, const int32_t& j) {
    sub1 = "";
    sub2 = "";
    if ((i + 1 < static_cast<int32_t>(lines.size())) && (i - 1 >= 0) && (j + 1 < static_cast<int32_t>(lines[0].size())) && (j - 1 >= 0)) {
        for (int x = -1; x < 2; x++) {
            sub1 += lines[i+x][j+x];
            sub2 += lines[i+x][j-x];
        }
        return true;
    } else {
        return false;
    }
}

bool d1_sub3(const vector<string>& lines, string& sub, const int32_t& i, const int32_t& j) {
    sub = "";
    if ((i + 3 < static_cast<int32_t>(lines.size())) && (j + 3 < static_cast<int32_t>(lines[0].size()))) {
        for (size_t x = 0; x < 4; x++) {
            sub += lines[i+x][j+x];
        }
        return true;
    } else {
        return false;
    }
}

bool d2_substring(const vector<string>& lines, string& sub, const int32_t& i, const int32_t& j) {
    sub = "";
    if ((i + 3 < static_cast<int32_t>(lines.size())) && (j - 3 >= 0)) {
        for (size_t x = 0; x < 4; x++) {
            sub += lines[i+x][j-x];
        }
        return true;
    } else {
        return false;
    }
}

int64_t d04pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    string sub;
    for (size_t i = 0; i < lines.size(); i++) {
        for (size_t j = 0; j < lines[0].size(); j++) {
            if (horizontal_substring(lines, sub, i, j)) {
                if ((sub == "XMAS") || sub == "SAMX") {
                    result++;
                }
            }
            if (vertical_substring(lines, sub, i, j)) {
                if ((sub == "XMAS") || sub == "SAMX") {
                    result++;
                }
            }
            if (d1_substring(lines, sub, i, j)) {
                if ((sub == "XMAS") || sub == "SAMX") {
                    result++;

                }
            }
            if (d2_substring(lines, sub, i, j)) {
                if ((sub == "XMAS") || sub == "SAMX") {
                    result++;
                }
            }
        }
    }
    return result;
}

int64_t d04pt2(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    string sub1;
    string sub2;
    for (size_t i = 0; i < lines.size(); i++) {
        for (size_t j = 0; j < lines[0].size(); j++) {
            if (subcross(lines, sub1, sub2, i, j)) {
                if (((sub1 == "MAS") || sub1 == "SAM") && ((sub2 == "MAS") || sub2 == "SAM")) {
                    result++;
                }
            }
        }
    }
    return result;
}