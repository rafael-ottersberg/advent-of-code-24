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

int64_t d09pt1(const filesystem::path& file_path) {
    auto line = read_lines(file_path)[0];
    int64_t result = 0;

    bool em = false;
    int file_index = 0;
    vector<int> filesystem;

    for (char c : line) {
        int file_size = c - '0';
        int ind = file_index;
        if (em) {
            ind = -1;
            em = false;
        } else {
            em = true;
            file_index++;
        }
        for (int j = 0; j < file_size; j++) {
            filesystem.push_back(ind);
        }
    }

    auto rit = filesystem.rbegin();
    for (auto it = filesystem.begin(); it != filesystem.end(); it++) {
        if (*it != -1) {
            continue;
        }
        while (*rit == -1) {
            rit++;
        }
        if (it >= rit.base()) {
            break;
        }
        *it = *rit;
        *rit = -1;
    }

    for (auto it = filesystem.cbegin(); it != filesystem.cend(); it++) {
        if (*it != -1) {
            result += distance(filesystem.cbegin(), it) * *it;
        }
    }

    return result;
}

int64_t d09pt2(const filesystem::path& file_path) {
    auto line = read_lines(file_path)[0];
    int64_t result = 0;

    bool em = false;
    int file_index = 0;
    vector<pair<int,int>> filesystem;

    for (char c : line) {
        int file_size = c - '0';
        int ind = file_index;
        if (em) {
            ind = -1;
            em = false;
        } else {
            em = true;
            file_index++;
        }
        filesystem.push_back(make_pair(ind, file_size));
    }

    for (auto rit = filesystem.rbegin(); rit != filesystem.rend(); rit++) {
        auto move = *rit;
        auto index = move.first;
        auto space = move.second;

        if (index == -1) continue;
        for (auto it = filesystem.begin(); it != filesystem.end(); it++) {
            if (it == rit.base()) break;
            auto target = *it;
            auto t_index = target.first;
            auto t_space  = target.second;
            if (t_index != -1) continue;
            if (t_space < space) continue;
            *it = *rit;
            *rit = make_pair(-1, space);
            auto d = distance(it, rit.base());
            if (t_space > space) {
                it = filesystem.insert(it+1, make_pair(-1, t_space-space));
                rit = make_reverse_iterator(it + d);
            }
            break;
        }
    }

    int i = 0;
    for (auto it = filesystem.cbegin(); it != filesystem.cend(); it++) {
        auto file = *it;
        for (int j = 0; j < file.second; j++){
            if (file.first != -1) {
                result += i * file.first;
            }
            i++;
        }
    }
    return result;
}