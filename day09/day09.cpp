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
    short file_index = 0;
    vector<short> filesystem;

    for (char c : line) {
        int file_size = c - '0';
        short ind = file_index;
        if (em) {
            ind = -1;
            em = false;
        } else {
            em = true;
            file_index++;
        }
        for (short j = 0; j < file_size; j++) {
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

struct file {
    short id;
    int size;
};

int64_t d09pt2(const filesystem::path& file_path) {
    auto line = read_lines(file_path)[0];
    int64_t result = 0;

    bool em = false;
    short file_index = 0;
    vector<file> filesystem;

    for (char c : line) {
        int file_size = c - '0';
        short ind = file_index;
        if (em) {
            ind = -1;
            em = false;
        } else {
            em = true;
            file_index++;
        }
        filesystem.push_back({ind, file_size});
    }

    for (auto rit = filesystem.rbegin(); rit != filesystem.rend(); rit++) {
        auto file = *rit;

        if (file.id == -1) continue;
        for (auto it = filesystem.begin(); it != filesystem.end(); it++) {
            if (it == rit.base()) break;
            auto target = *it;
            if (target.id != -1) continue;
            if (target.size < file.size) continue;
            *it = *rit;
            *rit = {-1, file.size};
            auto d = distance(it, rit.base());
            if (target.size > file.size) {
                it = filesystem.insert(it+1, {-1, target.size-file . size});
                rit = make_reverse_iterator(it + d);
            }
            break;
        }
    }

    int i = 0;
    for (auto it = filesystem.cbegin(); it != filesystem.cend(); it++) {
        auto file = *it;
        for (int j = 0; j < file.size; j++){
            if (file.id != -1) {
                result += i * file.id;
            }
            i++;
        }
    }
    return result;
}