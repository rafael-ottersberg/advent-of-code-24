#include <string>
#include <iostream>
#include <filesystem>
#include <functional>
#include <iomanip>

#include "util.hpp"

#include "day01/day01.hpp"
#include "day02/day02.hpp"
#include "day03/day03.hpp"
#include "day04/day04.hpp"
#include "day05/day05.hpp"
#include "day06/day06.hpp"
#include "day07/day07.hpp"
#include "day08/day08.hpp"
#include "day09/day09.hpp"
#include "day10/day10.hpp"
#include "day11/day11.hpp"
#include "day12/day12.hpp"
#include "day13/day13.hpp"
#include "day14/day14.hpp"
#include "day15/day15.hpp"
#include "day16/day16.hpp"
#include "day17/day17.hpp"
#include "day18/day18.hpp"
#include "day19/day19.hpp"
#include "day20/day20.hpp"
#include "day21/day21.hpp"
#include "day22/day22.hpp"
#include "day23/day23.hpp"
#include "day24/day24.hpp"
#include "day25/day25.hpp"

using Func = std::function<int64_t(const std::filesystem::path&)>;

std::map<int, std::pair<Func, Func>> solutions = {
    {1, std::make_pair(d01pt1, d01pt2)},
    {2, std::make_pair(d02pt1, d02pt2)},
    {3, std::make_pair(d03pt1, d03pt2)},
    {4, std::make_pair(d04pt1, d04pt2)},
    {5, std::make_pair(d05pt1, d05pt2)},
    {6, std::make_pair(d06pt1, d06pt2)},
    {7, std::make_pair(d07pt1, d07pt2)},
    {8, std::make_pair(d08pt1, d08pt2)},
    {9, std::make_pair(d09pt1, d09pt2)},
    {10, std::make_pair(d10pt1, d10pt2)},
    {11, std::make_pair(d11pt1, d11pt2)},
    {12, std::make_pair(d12pt1, d12pt2)},
    {13, std::make_pair(d13pt1, d13pt2)},
    {14, std::make_pair(d14pt1, d14pt2)},
    {15, std::make_pair(d15pt1, d15pt2)},
    {16, std::make_pair(d16pt1, d16pt2)},
    {17, std::make_pair(d17pt1, d17pt2)},
    {18, std::make_pair(d18pt1, d18pt2)},
    {19, std::make_pair(d19pt1, d19pt2)},
    {20, std::make_pair(d20pt1, d20pt2)},
    {21, std::make_pair(d21pt1, d21pt2)},
    {22, std::make_pair(d22pt1, d22pt2)},
    {23, std::make_pair(d23pt1, d23pt2)},
    {24, std::make_pair(d24pt1, d24pt2)},
    {25, std::make_pair(d25pt1, d25pt2)},
};


int main(int argc, char* argv[]) {
    auto aoc_path = std::filesystem::path("/home/rafael/advent-of-code-24"); // change on different machine
    int d;
    if (argc > 1) {
        d = std::stoi(argv[1]);
    } else {
        auto now = std::chrono::system_clock::now();
        std::time_t now_time = std::chrono::system_clock::to_time_t(now);
        std::tm* now_tm = std::localtime(&now_time);
        d = now_tm->tm_mday; // Get the current day of the month
        if (d > 25) d = 25;
    }

    std::ostringstream day_stream;
    day_stream << "day" << std::setw(2) << std::setfill('0') << d;
    std::string day = day_stream.str();

    auto folder_path = aoc_path / day;
    std::cout << "Day: " << d << std::endl;
    std::cout << "Pt 1:" << std::endl;
    std::cout << time_function(solutions[d].first, folder_path / "test.txt") << std::endl;
    std::cout << time_function(solutions[d].first, folder_path / "input.txt") << std::endl;
    std::cout << "Pt 2:" << std::endl;
    std::cout << time_function(solutions[d].second, folder_path / "test.txt") << std::endl;
    std::cout << time_function(solutions[d].second, folder_path / "input.txt") << std::endl;
    return 0;
}
