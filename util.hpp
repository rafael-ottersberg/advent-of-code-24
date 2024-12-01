#ifndef UTIL_H
#define UTIL_H

#include <vector>
#include <string>
#include <functional>
#include <chrono>
#include <iostream>
#include <filesystem>
#include <fstream>
#include <regex>
#include <algorithm>

inline std::vector<std::string> read_lines(const std::filesystem::path& filepath) {
    std::vector<std::string> lines;

    std::fstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "Failed to open file: " << filepath << std::endl;
        return lines;
    }

    std::string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    file.close();

    if (!lines.empty() && lines.back().empty()) {
        lines.pop_back();
    }

    return lines;
}

inline std::vector<int> convert_to_int(const std::vector<std::string>& number_strings) {
    std::vector<int> numbers;
    std::transform(number_strings.begin(), number_strings.end(), std::back_inserter(numbers), [](const std::string& nst) {return stoi(nst); });
    return numbers;
}

inline std::vector<long> convert_to_long(const std::vector<std::string>& number_strings) {
    std::vector<long> numbers;
    std::transform(number_strings.begin(), number_strings.end(), std::back_inserter(numbers), [](const std::string& nst) {return stol(nst); });
    return numbers;
}

inline bool contains_substr(const std::string& target, const std::string& sub) {
    bool found = target.find(sub) != std::string::npos;
    return found;
}

inline std::vector<std::string> split(const std::string& line, const std::string delimiter) {
    std::vector<std::string> splitted;
    
    size_t start = 0;
    size_t end = line.find(delimiter);

    size_t del_size = delimiter.size();

    while (end != std::string::npos) {
        splitted.push_back(line.substr(start, end - start));
        start = end + del_size;
        end = line.find(delimiter, start);
    }
    splitted.push_back(line.substr(start));

    return splitted;
}

inline std::vector<std::string> split_regex(const std::string& line, const std::string& regex_delimiter = "\\s+") {
    std::vector<std::string> splitted;
    std::regex re(regex_delimiter);
    std::sregex_token_iterator it(line.begin(), line.end(), re, -1);
    std::sregex_token_iterator reg_end;

    for (; it != reg_end; ++it) {
        std::string s = it->str();
        if (s != "") {
            splitted.push_back(it->str());
        }
    }

    return splitted;
}

template<typename Func, typename... Args>
inline auto time_function(Func func, Args&&... args) {
    auto start = std::chrono::high_resolution_clock::now();
    auto ret = func(std::forward<Args>(args)...);
    auto end = std::chrono::high_resolution_clock::now();
    
    std::chrono::duration<double> dur = end - start;
    std::cout << dur.count() * 1000 << " ms" << std::endl;
    return ret;
}

inline void hash_combine(std::size_t& seed, std::size_t value) {
    seed ^= value + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

struct tup2_hash {
    template <typename T1, typename T2>
    size_t operator()(const std::tuple<T1, T2>& t) const {
        auto h1 = std::hash<T1>{}(std::get<0>(t));
        auto h2 = std::hash<T2>{}(std::get<1>(t));
        size_t seed = 0;
        hash_combine(seed, h1);
        hash_combine(seed, h2);
        return seed;
    }
};

struct tup2_equal {
    template <typename T1, typename T2>
    bool operator()(const std::tuple<T1, T2>& t1, const std::tuple<T1, T2>& t2) const {
        return std::get<0>(t1) == std::get<0>(t2) && std::get<1>(t1) == std::get<1>(t2);
    }
};

#endif //UTIL_H