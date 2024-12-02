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


bool check_series(const vector<int>& li, int depth, int threshold) {
    for (int i = 1; i < li.size(); i++) {
        int diff = li[i] - li[i - 1];
        if ((0 < diff) && (diff < 4)) {
            continue;
        }
        else {
            if (depth < threshold) {
                auto li1 = li;
                li1.erase(li1.begin() + i - 1);
                
                auto li2 = li;
                li2.erase(li2.begin() + i);

                return (check_series(li1, 1, threshold) || check_series(li2, 1, threshold));
            }
            else {
                return false;
            }
        }
    }
    return true;
}

int64_t d02pt1(const filesystem::path& file_path) {
    //cout << endl << "Day 02 - Pt1: " << file_path.filename() << endl;
    auto lines = read_lines(file_path);
    int64_t result = 0;

    for (auto line : lines) {
        auto li = convert_to_int32(split(line, " "));
        auto p = check_series(li, 0, 0);
        transform(li.cbegin(), li.cend(), li.begin(), std::negate<int>());
        auto n = check_series(li, 0, 0);

        if (p || n) {
            result++;
        }

    }
    return result;
}

int64_t d02pt2(const filesystem::path& file_path) {
    //cout << endl << "Day 02 - Pt2: " << file_path.filename() << endl;
    auto lines = read_lines(file_path);
    int64_t result = 0;

    for (auto line : lines) {
        auto li = convert_to_int32(split(line, " "));
        auto p = check_series(li, 0, 1);
        transform(li.cbegin(), li.cend(), li.begin(), std::negate<int>());
        auto n = check_series(li, 0, 1);

        if (p || n) {
            result++;
        }

    }
    return result;
}
