#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <filesystem>
#include <numeric>
#include <cstdint>
#include <regex>

#include "util.hpp"

using namespace std;

unordered_set<pair<int, int>, pair_hash> search_trail(const pair<int, int>& coor, const vector<string>& grid) {
    unordered_set<pair<int, int>, pair_hash> peaks;
    auto current_height = grid[coor.first][coor.second];
    if (current_height == '9') {
        peaks.insert(coor);
        return peaks;
    } 

    array<pair<int,int>, 4> directions = {
        make_pair(-1, 0), make_pair(1, 0), 
        make_pair(0, -1), make_pair(0, 1)};

    for (auto d : directions) {
        auto coor_candidate = coor + d;
        if (is_on_grid(coor_candidate, grid)) {
            if (grid[coor_candidate.first][coor_candidate.second] - current_height == 1) {
                auto peaks_c = search_trail(coor_candidate, grid);
                peaks.insert(peaks_c.begin(), peaks_c.end());
            }
        }
    }
    return peaks;
}

int search_trail2(const pair<int, int>& coor, const vector<string>& grid) {
    auto current_height = grid[coor.first][coor.second];
    if (current_height == '9') {
        return 1;
    } 

    array<pair<int,int>, 4> directions = {
        make_pair(-1, 0), make_pair(1, 0), 
        make_pair(0, -1), make_pair(0, 1)};

    int result = 0;
    for (auto d : directions) {
        auto coor_candidate = coor + d;
        if (is_on_grid(coor_candidate, grid)) {
            if (grid[coor_candidate.first][coor_candidate.second] - current_height == 1) {
                result += search_trail2(coor_candidate, grid);
            }
        }
    }
    return result;
}

int64_t d10pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    for (auto l_it = lines.begin(); l_it != lines.end(); l_it++) {
        auto line = *l_it;
        for (auto c_it = line.begin(); c_it != line.end(); c_it++) {
            auto c = *c_it;
            if (c == '0') {
                auto i = distance(lines.begin(), l_it);
                auto j = distance(line.begin(), c_it);
                auto coor = make_pair(i, j);
                auto result_tiles = search_trail(coor, lines);
                result += result_tiles.size();
            }
        }
    }
    return result;
}

int64_t d10pt2(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    for (auto l_it = lines.begin(); l_it != lines.end(); l_it++) {
        auto line = *l_it;
        for (auto c_it = line.begin(); c_it != line.end(); c_it++) {
            auto c = *c_it;
            if (c == '0') {
                auto i = distance(lines.begin(), l_it);
                auto j = distance(line.begin(), c_it);
                auto coor = make_pair(i, j);
                result += search_trail2(coor, lines);
            }
        }
    }
    return result;
}