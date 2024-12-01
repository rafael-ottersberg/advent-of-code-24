#include <string>
#include <iostream>
#include <filesystem>
#include "util.hpp"
#include "day01/day01.hpp"

int main() {
    auto aoc_path = std::filesystem::path("C:\\Users\\rafae\\\Documents\\code\\advent-of-code-24\\"); // change on different machine

    auto folder_path = aoc_path / "day01";

    std::cout << time_function(d01pt1, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d01pt1, folder_path / "input.txt") << std::endl;
    std::cout << time_function(d01pt2, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d01pt2, folder_path / "input.txt") << std::endl;
    return 0;
}