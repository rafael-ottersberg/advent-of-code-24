import os
import sys
import pathlib
from collections import Counter

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

sys.setrecursionlimit(1000000)

from helper import *

def walk(c, grid, path):
    x = c[0]
    y = c[1]
    letter = grid[x][y]
    if letter == 'E':
        path[c] = 0
        return 0
    
    for d in ADJ4:
        nx, ny = x + d[0], y + d[1]
        nl = grid[nx][ny]
        if nl != "#" and (nx, ny) not in path:
            path[(nx, ny)] = None
            dist = walk((nx, ny), grid, path) + 1
            path[(x, y)] = dist
            return dist

def solution(input_file):
    result = 0
    grid = open(input_file, 'r').read().splitlines()
    #find start
    start = (0,0)
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i,j)
                break
        else:
            continue
        break

    path = dict()
    path[start] = None
    result = walk(start, grid, path)
    path[start] = result

    discounts = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == "#":
                pc = (i-1, j)
                nc1 = (i+1, j)
                nc2 = (i+2, j)
                if pc in path:
                    if nc1 in path:
                        discount = abs(path[nc1]-path[pc]) - 2
                        discounts.append(discount)
                    elif nc2 in path:
                        discount = abs(path[nc2]-path[pc]) - 3
                        discounts.append(discount)
                pc = (i, j-1)
                nc1 = (i, j+1)
                nc2 = (i, j+2)
                if pc in path:
                    if nc1 in path:
                        discount = abs(path[nc1]-path[pc]) - 2
                        discounts.append(discount)
                    elif nc2 in path:
                        discount = abs(path[nc2]-path[pc]) - 3
                        discounts.append(discount)

    result = 0
    discounts.sort()
    count = Counter(discounts)
    for c in count:
        if c >= 100:
            result += count[c]

    return result

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solution2(input_file):
    result = 0
    grid = open(input_file, 'r').read().splitlines()
    #find start
    start = (0,0)
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i,j)
                break
        else:
            continue
        break

    path = dict()
    path[start] = None
    result = walk(start, grid, path)
    path[start] = result

    discounts = []
    for p1 in path:
        for p2 in path:
            if path[p1] > path[p2]:
                d = dist(p1, p2)
                if d <= 20:
                    discount = path[p1] - path[p2] - d
                    if discount >= 100:
                        discounts.append(discount)

    #count = Counter(discounts)
    #ke = [k for k in count]
    #ke.sort()
    #for k in ke:
    #    print(count[k], k)

    return len(discounts)

#  893328 low

# 1027091 high
# 1150073 high


if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 0: # run part 1
        print(benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))