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
#include <queue>

#include "util.hpp"

using namespace std;

struct page {
    public:
        int value;
        static unordered_map<int, vector<int>> order_graph;

        page(int val) : value(val) {}

        bool operator<(const page& other) const {
            auto larger_elements = order_graph[value];
            return (find(larger_elements.begin(), larger_elements.end(), other.value) != larger_elements.end());
        }

        static void update_ordering(const unordered_map<int, vector<int>>& new_ordering) {
            order_graph = new_ordering;
        }
};

unordered_map<int, vector<int>> page::order_graph;


int64_t d05pt1(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    unordered_map<int, vector<int>> order_graph;
    vector<vector<page>> pages_list;

    bool pt2 = false;
    for (auto line : lines) {
        if (line.empty()) {
            pt2 = true;
        } else if (!pt2) {
            auto pair = convert_to_int32(split(line, "|"));
            order_graph[pair[0]].push_back(pair[1]);
            if (order_graph.find(pair[1]) == order_graph.end()) {
                order_graph[pair[1]];
            }
        } else {
            auto nstr = split(line, ",");
            vector<page> pages;
            for (auto n : nstr) {
                pages.push_back(page(stoi(n)));
            }
            pages_list.push_back(pages);
        }   
    }
    page::update_ordering(order_graph);

    for (auto pages : pages_list) {
        if (is_sorted(pages.cbegin(), pages.cend())) {
            result += pages[(pages.size() - 1) / 2].value;
        }
    }

    return result;
}

int64_t d05pt2(const filesystem::path& file_path) {
    auto lines = read_lines(file_path);
    int result = 0;

    unordered_map<int, vector<int>> order_graph;
    vector<vector<page>> pages_list;

    bool pt2 = false;
    for (auto line : lines) {
        if (line.empty()) {
            pt2 = true;
        } else if (!pt2) {
            auto pair = convert_to_int32(split(line, "|"));
            order_graph[pair[0]].push_back(pair[1]);
            if (order_graph.find(pair[1]) == order_graph.end()) {
                order_graph[pair[1]];
            }
        } else {
            auto nstr = split(line, ",");
            vector<page> pages;
            for (auto n : nstr) {
                pages.push_back(page(stoi(n)));
            }
            pages_list.push_back(pages);
        }   
    }
    page::update_ordering(order_graph);

    for (auto pages : pages_list) {
        if (!is_sorted(pages.cbegin(), pages.cend())) {
            sort(pages.begin(), pages.end());
            result += pages[(pages.size() - 1) / 2].value;
        }
    }

    return result;
}