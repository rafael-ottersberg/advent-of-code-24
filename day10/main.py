import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def is_on_grid(i, j, lines):
    return 0 <= i < len(lines) and 0 <= j < len(lines[0])

def search_trails(i, j, grid):
    current = grid[i][j]
    if current == 9:
        s = set()
        s.add((i,j))
        return s
    
    possible_paths = set()
    for d in [-1, 1]:
        ci, cj = (i + d, j)
        if is_on_grid(ci, cj, grid):
            if (grid[ci][cj] - current) == 1:
                possible_paths = possible_paths.union(search_trails(ci, cj, grid))

        ci, cj = (i, j + d)
        if is_on_grid(ci, cj, grid):
            if (grid[ci][cj] - current) == 1:
                possible_paths = possible_paths.union(search_trails(ci, cj, grid))
                
    return possible_paths

def search_trails2(i, j, grid):
    current = grid[i][j]
    if current == 9:
        return 1
    
    possible_paths = 0
    for d in [-1, 1]:
        ci, cj = (i + d, j)
        if is_on_grid(ci, cj, grid):
            if (grid[ci][cj] - current) == 1:
                possible_paths += search_trails2(ci, cj, grid)

        ci, cj = (i, j + d)
        if is_on_grid(ci, cj, grid):
            if (grid[ci][cj] - current) == 1:
                possible_paths += search_trails2(ci, cj, grid)
                
    return possible_paths


def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    trailheads = []
    grid = []
    for i, line in enumerate(lines):
        row = []
        for j, c in enumerate(line):
            row.append(int(c))
            if c == "0":
                trailheads.append((i,j))
        grid.append(row)
    
    for t in trailheads:
        r = search_trails(t[0], t[1], grid)
        i = len(r)
        result += i

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    trailheads = []
    grid = []
    for i, line in enumerate(lines):
        row = []
        for j, c in enumerate(line):
            row.append(int(c))
            if c == "0":
                trailheads.append((i,j))
        grid.append(row)
    
    for t in trailheads:
        result += search_trails2(t[0], t[1], grid)

    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))