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

int64_t d08pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    unordered_map<char, vector<pair<int,int>>> letters;
    for (size_t i = 0; i < lines.size(); i++) {
        auto line = lines[i];
        for (size_t j = 0; j < line.size(); j++) {
            auto c = line[j];
            if (c == '.') {
                continue;
            } else {
                letters[c].push_back(make_pair(i, j));
            }
        }
    }
    
    unordered_set<pair<int,int>, pair_hash> positions;
    for (auto kv : letters) {
        for (auto p1 : kv.second) {
            for (auto p2 : kv.second) {
                if (p1 == p2) {
                    continue;
                } else {
                    auto d = p2 - p1;

                    auto t = p1 - d;
                    if (is_on_grid(t, lines)) {
                        positions.insert(t);
                    }

                    t = p2 + d;
                    if (is_on_grid(t, lines)) {
                        positions.insert(t);
                    }
                }
            }
        }
    }
    return positions.size();
}

int64_t d08pt2(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    unordered_map<char, vector<pair<int,int>>> letters;
    for (size_t i = 0; i < lines.size(); i++) {
        auto line = lines[i];
        for (size_t j = 0; j < line.size(); j++) {
            auto c = line[j];
            if (c == '.') {
                continue;
            } else {
                letters[c].push_back(make_pair(i, j));
            }
        }
    }
    
    unordered_set<pair<int,int>, pair_hash> positions;
    for (auto kv : letters) {
        for (auto p1 : kv.second) {
            for (auto p2 : kv.second) {
                if (p1 == p2) {
                    continue;
                } else {
                    auto d = p2 - p1;
                                        
                    int i = 0;
                    while (true){
                        auto t = p1 - i * d;

                        if (is_on_grid(t, lines)) {
                            positions.insert(t);
                        } else {
                            break;
                        }
                        i++;
                    }

                    i = 0;  
                    while (true) {
                        auto t = p2 + i * d;

                        if (is_on_grid(t, lines)) {
                            positions.insert(t);
                        } else {
                            break;
                        }
                        i++;
                    }
                }
            }
        }
    }
    return positions.size();
}