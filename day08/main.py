import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def on_grid(coor, grid):
    if 0 <= coor[0] < len(grid) and 0 <= coor[1] < len(grid[0]):
        return True

    return False
    

def solution(input_file):
    lines = open(input_file, 'r').read().splitlines()

    letters = {}
    for i, line in enumerate(lines):
        for j, line in enumerate(line):
            letter = lines[i][j]
            if letter == ".":
                continue
            
            if letter in letters:
                letters[letter].append((i, j))
            else:
                letters[letter] = [(i, j)]

    positions = set()

    for letter in letters:
        for c in letters[letter]:
            for c2 in letters[letter]:
                if c != c2:
                    di = c2[0] - c[0]
                    dj = c2[1] - c[1]
                    
                    t1 = (c[0] - di, c[1] - dj)
                    if on_grid(t1, lines):
                        positions.add(t1)
                    
                    t2 = (c2[0] + di, c2[1] + dj)
                    if on_grid(t2, lines):
                        positions.add(t2)

    return len(positions)

def solution2(input_file):
    lines = open(input_file, 'r').read().splitlines()

    letters = {}
    for i, line in enumerate(lines):
        for j, line in enumerate(line):
            letter = lines[i][j]
            if letter == ".":
                continue
            
            if letter in letters:
                letters[letter].append((i, j))
            else:
                letters[letter] = [(i, j)]

    positions = set()

    for letter in letters:
        for c in letters[letter]:
            for c2 in letters[letter]:
                if c != c2:
                    di = c2[0] - c[0]
                    dj = c2[1] - c[1]
                    i = 0
                    while True:
                        t1 = (c[0] - i * di, c[1] - i * dj)
                        i += 1

                        if on_grid(t1, lines):
                            positions.add(t1)
                        else:
                            break
                    i = 0
                    while True:
                        t2 = (c2[0] + i * di, c2[1] + i * dj)
                        i += 1
                        if on_grid(t2, lines):
                            positions.add(t2)
                        else:
                            break
                        
    return len(positions)

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 0: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))