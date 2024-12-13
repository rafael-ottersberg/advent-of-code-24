#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <array>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <filesystem>
#include <numeric>
#include <cstdint>
#include <regex>
#include <queue>

#include "util.hpp"

using namespace std;

const array<pair<int,int>, 4> ADJ4 = {
    make_pair( 1,  0),
    make_pair(-1,  0),
    make_pair( 0,  1),
    make_pair( 0, -1)
};

int explore(
    pair<int,int>& c, const vector<string>& grid, 
    unordered_set<pair<int,int>, pair_hash>& explored) {

    unordered_set<pair<int,int>, pair_hash> region;

    queue<pair<int,int>> q;
    unordered_set<pair<int,int>, pair_hash> in_q;
    q.push(c);
    region.insert(c);

    char value = grid[c.first][c.second];
    int edge_count = 0;
    int neighbour_count;

    while (!q.empty()) {
        auto tc = q.front();
        q.pop();
        neighbour_count = 0;
        for (auto d : ADJ4) {
            auto nc = tc + d;
            if (is_on_grid(nc, grid) && grid[nc.first][nc.second] == value) {
                neighbour_count += 1;
                if (!region.contains(nc)) {
                    q.push(nc);
                    region.insert(nc);
                }
            }
        }
        edge_count += 4 - neighbour_count;
    }
    explored.insert(region.begin(), region.end());
    return region.size() * edge_count;
}

int find_edges(
    pair<int,int>& c, const vector<string>& grid, 
    unordered_set<pair<int,int>, pair_hash>& explored, 
    unordered_map<
        pair<int,int>, 
        unordered_set<pair<int,int>, pair_hash>, 
        pair_hash>& edges) {

    unordered_set<pair<int,int>, pair_hash> region;

    queue<pair<int,int>> q;
    unordered_set<pair<int,int>, pair_hash> in_q;
    q.push(c);
    region.insert(c);

    char value = grid[c.first][c.second];

    while (!q.empty()) {
        auto tc = q.front();
        q.pop();
        for (auto d : ADJ4) {
            auto nc = tc + d;
            if (is_on_grid(nc, grid) && grid[nc.first][nc.second] == value) {
                if (!region.contains(nc)) {
                    q.push(nc);
                    region.insert(nc);
                }
            } else {
                edges[d].insert(nc);
            }
        }
    }
    explored.insert(region.begin(), region.end());
    return region.size();
}

int64_t d12pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    unordered_set<pair<int,int>, pair_hash> explored;

    for (auto l_it = lines.begin(); l_it != lines.end(); l_it++) {
        auto line = *l_it;
        for (auto c_it = line.begin(); c_it != line.end(); c_it++) {
            int i = distance(lines.begin(), l_it);
            int j = distance(line.begin(), c_it);
            auto p = make_pair(i, j);
            if (!explored.contains(p)) {
                result += explore(p, lines, explored);
            }
        }
    }
    return result;
}

int64_t d12pt2(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    unordered_set<pair<int,int>, pair_hash> explored;

    for (auto l_it = lines.begin(); l_it != lines.end(); l_it++) {
        auto line = *l_it;
        for (auto c_it = line.begin(); c_it != line.end(); c_it++) {
            int i = distance(lines.begin(), l_it);
            int j = distance(line.begin(), c_it);
            auto p = make_pair(i, j);
            
            unordered_map<pair<int,int>, unordered_set<pair<int,int>, pair_hash>, pair_hash> edges;
            int area = 0;
            if (!explored.contains(p)) {
                area = find_edges(p, lines, explored, edges);
            }
            int sides = 0;
            for (auto d_e : edges) {
                auto d = d_e.first;
                auto edge_dir = make_pair(d.second, d.first);
                auto edges = d_e.second;
                for (auto e : edges) {
                    if (!edges.contains(e - edge_dir)) {
                        sides++;
                    }
                }
            }
            result += area * sides;
        }
    }

    return result;
}