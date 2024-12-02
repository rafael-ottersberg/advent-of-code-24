#include <string>
#include <iostream>
#include <filesystem>
#include "util.hpp"

#include "day01/day01.hpp"
#include "day02/day02.hpp"

int main() {
    auto aoc_path = std::filesystem::path("C:\\Users\\ro22p291\\code\\advent-of-code-24\\"); // change on different machine

    auto folder_path = aoc_path / "day02";

    std::cout << time_function(d02pt1, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d02pt1, folder_path / "input.txt") << std::endl;
    std::cout << time_function(d02pt2, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d02pt2, folder_path / "input.txt") << std::endl;
    return 0;
}