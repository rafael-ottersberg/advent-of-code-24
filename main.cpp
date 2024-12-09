#include <string>
#include <iostream>
#include <filesystem>
#include "util.hpp"
#include "day07p/day07.hpp"

int main() {
    auto aoc_path = std::filesystem::path("/home/rafael/advent-of-code-24"); // change on different machine

    auto folder_path = aoc_path / "day07";

    std::cout << "Pt 1:" << std::endl;
    std::cout << "CPU:" << std::endl;
    std::cout << time_function(d07pt1, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d07pt1, folder_path / "input.txt") << std::endl;
    std::cout << "GPU:" << std::endl;
    time_function(d07pt1cu, folder_path / "test.txt");
    std::cout << time_function(d07pt1cu, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d07pt1cu, folder_path / "input.txt") << std::endl;
    std::cout << "Pt 2:" << std::endl;
    std::cout << "CPU:" << std::endl;
    std::cout << time_function(d07pt2, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d07pt2, folder_path / "input.txt") << std::endl;
    std::cout << "GPU:" << std::endl;
    std::cout << time_function(d07pt2cu, folder_path / "test.txt") << std::endl;
    std::cout << time_function(d07pt2cu, folder_path / "input.txt") << std::endl;
    return 0;
}