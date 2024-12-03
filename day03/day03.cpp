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


int64_t d03pt1(const filesystem::path& file_path) {
    //cout << endl << "Day 03 - Pt1: " << file_path.filename() << endl;
    auto lines = read_lines(file_path);
    int result = 0;

    regex r(R"(mul\(([0-9]+),([0-9]+)\))");
    smatch m;

    bool enabled = true;
    for (auto line : lines) {
        string::const_iterator searchStart(line.cbegin());

        while (regex_search(searchStart, line.cend(), m, r)) {
            result += stoi(m[1]) * stoi(m[2]);
            searchStart = m.suffix().first;
        }
        

    }
    return result;
}

int64_t d03pt2(const filesystem::path& file_path) {
    //cout << endl << "Day 03 - Pt2: " << file_path.filename() << endl;
    auto lines = read_lines(file_path);
    int result = 0;

    regex r(R"(mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\))");
    smatch m;

    bool enabled = true;
    for (auto line : lines) {
        string::const_iterator searchStart(line.cbegin());

        while (regex_search(searchStart, line.cend(), m, r)) {
            if (m[0] == "do()") { enabled = true; }
            else if (m[0] == "don't()") { enabled = false; }
            else if (enabled) { result += stoi(m[1]) * stoi(m[2]); }
            searchStart = m.suffix().first;
        }

    }
    return result;
}