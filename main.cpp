#include <string>
#include <iostream>
#include <filesystem>
#include "util.hpp"
#include "day04/day04.hpp"

int main() {
    auto aoc_path = std::filesystem::path("/home/rafael/advent-of-code-24"); // change on different machine

    auto folder_path = aoc_path / "day04";

    std::cout << "Pt 1:" << std::endl;
    std::cout << time_function(d04pt1, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d04pt1, folder_path / "input.txt") << std::endl;
    std::cout << "Pt 2:" << std::endl;
    std::cout << time_function(d04pt2, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d04pt2, folder_path / "input.txt") << std::endl;
    return 0;
}