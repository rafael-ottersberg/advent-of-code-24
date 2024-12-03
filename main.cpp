#include <string>
#include <iostream>
#include <filesystem>
#include "util.hpp"
#include "day03/day03.hpp"

int main() {
    auto aoc_path = std::filesystem::path("C:\\Users\\ro22p291\\code\\advent-of-code-24\\"); // change on different machine

    auto folder_path = aoc_path / "day03";

    std::cout << time_function(d03pt1, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d03pt1, folder_path / "input.txt") << std::endl;
    std::cout << time_function(d03pt2, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d03pt2, folder_path / "input.txt") << std::endl;
    return 0;
}