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
#include <cstdint>

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

inline std::vector<std::int64_t> convert_to_int64(const std::vector<std::string>& number_strings) {
    std::vector<std::int64_t> numbers;
    std::transform(number_strings.begin(), number_strings.end(), std::back_inserter(numbers), [](const std::string& nst) {return stoll(nst); });
    return numbers;
}

inline std::vector<std::int32_t> convert_to_int32(const std::vector<std::string>& number_strings) {
    std::vector<std::int32_t> numbers;
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

inline bool is_on_grid(int i, int j, const std::vector<std::string>& lines) {
    return i >= 0 && i < static_cast<int>(lines.size()) &&
           j >= 0 && j < static_cast<int>(lines[i].size());
}

inline bool is_on_grid(std::pair<int,int> coor, const std::vector<std::string>& lines) {
    auto i = coor.first;
    auto j = coor.second;
    return i >= 0 && i < static_cast<int>(lines.size()) &&
           j >= 0 && j < static_cast<int>(lines[i].size());
}

template<typename Func, typename... Args>
inline auto time_function(Func func, Args&&... args) {
    auto start = std::chrono::high_resolution_clock::now();
    auto ret = func(std::forward<Args>(args)...);
    auto end = std::chrono::high_resolution_clock::now();
    
    std::chrono::duration<double> dur = end - start;
    float d = dur.count();
    if (d >= 1.0f) {
        
    std::cout << std::fixed << std::setprecision(2);
        std::cout << d << " s" << std::endl;
    } else if (d * 1e3f >= 1.0f) {
        std::cout << std::fixed << std::setprecision(1);
        std::cout << d * 1e3f << " ms" << std::endl;
    } else {
        std::cout << std::fixed << std::setprecision(0);
        std::cout << d * 1e6f << " us" << std::endl;
    }
    return ret;
}

inline void hash_combine(std::size_t& seed, std::size_t value) {
    seed ^= value + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

struct pair_hash {
    template <typename T1, typename T2>
    size_t operator()(const std::pair<T1, T2>& t) const {
        auto h1 = std::hash<T1>{}(t.first);
        auto h2 = std::hash<T2>{}(t.second);
        size_t seed = 0;
        hash_combine(seed, h1);
        hash_combine(seed, h2);
        return seed;
    }
};

template <typename T,typename U>                                                   
std::pair<T,U> operator+(const std::pair<T,U> & l,const std::pair<T,U> & r) {   
    return {l.first+r.first,l.second+r.second};                                    
}

template <typename T,typename U>                                                   
std::pair<T,U> operator-(const std::pair<T,U> & l,const std::pair<T,U> & r) {   
    return {l.first-r.first,l.second-r.second};
}

template <typename T,typename U, typename V>                                                   
std::pair<T,U> operator*(const V& l,const std::pair<T,U> & r) {   
    return {l * r.first, l * r.second};
}    

#endif //UTIL_H