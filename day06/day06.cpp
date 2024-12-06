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
#include <queue>

#include "util.hpp"

using namespace std;

struct coor_dir {
    int16_t x;
    int16_t y;
    int16_t dx;
    int16_t dy;
};

union coor {
    coor_dir data;
    int64_t value;

    bool operator==(const coor& other) const {
        return value == other.value;
    }
};

namespace std {
    template <>
    struct hash<coor> {
        size_t operator()(const coor& c) const {
            // Combine the hash of the int64_t value
            return hash<int64_t>{}(c.value);
        }
    };
}

void turn_right(short& di, short& dj) {
    if ((di == -1) && (dj == 0)) {
        di = 0;
        dj = 1;
    } else if ((di == 0) && (dj == 1)) {
        di = 1;
        dj = 0;
    } else if ((di == 1) && (dj == 0)) {
        di = 0;
        dj = -1;
    } else if ((di == 0) && (dj == -1)) {
        di = -1;
        dj = 0;
    }
}

char get_c(const int& i, const int& j, const vector<string>& lines) {
    if (is_on_grid(i, j, lines)) {
        return lines[i][j];
    } else {
        return 0;
    }
}

int64_t d06pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int si = 0, sj = 0;

    for (size_t i = 0; i < lines.size(); i++) {
        auto line = lines[i];
        auto start = find(line.cbegin(), line.cend(), '^');
        if (start != line.cend()) {
            si = i;
            sj = distance(line.cbegin(), start);
            break;
        }
    }

    int i = si, j = sj;
    short di = -1, dj = 0;
    int ni, nj;
    char nc;

    unordered_set<pair<int,int>, pair_hash> seen;

    while (true) {
        ni = i + di;
        nj = j + dj;
        nc = get_c(ni, nj, lines);
        if (nc) {
            if (nc =='#') {
                turn_right(di, dj);
            } else{
                i = ni;
                j = nj;
                seen.insert(make_pair(i, j));
            }
        } else {
            break;
        }

    }

    return seen.size();
}

int64_t d06pt2(const filesystem::path& file_path) {
auto lines = read_lines(file_path);
    int result = 0;

    short si = 0, sj = 0;

    for (size_t i = 0; i < lines.size(); i++) {
        auto line = lines[i];
        auto start = find(line.cbegin(), line.cend(), '^');
        if (start != line.cend()) {
            si = i;
            sj = distance(line.cbegin(), start);
            break;
        }
    }

    for (size_t ti = 0; ti < lines.size(); ti++) {
        for (size_t tj = 0; tj < lines[0].size(); tj++){
            short i = si, j = sj;
            short di = -1, dj = 0;
            short ni, nj;
            char nc;
            auto test_lines = lines;
            if (test_lines[ti][tj] == '#' || test_lines[ti][tj] == '^') {
                continue;
            }
            test_lines[ti][tj] = '#';
            unordered_set<coor> travelled;

            while (true) {
                coor cd;
                cd.data = {i, j, di, dj};

                if (travelled.contains(cd)) {
                    result++;
                    break;
                }
                ni = i + di;
                nj = j + dj;
                nc = get_c(ni, nj, test_lines);
                if (nc) {
                    if (nc =='#') {
                        turn_right(di, dj);
                    } else{
                        travelled.insert(cd);
                        i = ni;
                        j = nj;
                    }
                } else {
                    break;
                }
            }            
        }
    }

    return result;
}