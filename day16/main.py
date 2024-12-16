import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *
from heapq import *

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    walls = set()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                walls.add((i,j))
            if c == "S":
                start = (i,j)
            if c == "E":
                end = (i,j)

    h = [(0, start, (0,1))]
    heapify(h)
    explored = set()

    while h:
        c, p, d = heappop(h)
        explored.add((p,d))
        if p == end:
            return c
        
        sp = (p[0]+d[0], p[1]+d[1])
        if sp not in walls and (sp, d) not in explored:
            heappush(h, (c+1, sp, d))

        dl = turn_left(d[0], d[1])
        sp = (p[0]+dl[0], p[1]+dl[1])
        if sp not in walls and (sp, dl) not in explored:
            heappush(h, (c+1001, sp, dl))

        dr = turn_right(d[0], d[1])
        sp = (p[0]+dr[0], p[1]+dr[1])
        if sp not in walls and (sp, dr) not in explored:
            heappush(h, (c+1001, sp, dr))

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    walls = set()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                walls.add((i,j))
            if c == "S":
                start = (i,j)
            if c == "E":
                end = (i,j)

    h = [(0, start, (0,1), set())]
    heapify(h)
    explored = set()
    result_tiles = set()
    solution = float('inf')

    while h:
        c, p, d, l = heappop(h)
        if c > solution:
            break
        explored.add((p,d))
        if p == end:
            result_tiles |= l
            solution = c
        
        sp = (p[0]+d[0], p[1]+d[1])
        if sp not in walls and (sp, d) not in explored:
            l = l.copy()
            l.add(p)
            heappush(h, (c+1, sp, d, l))

        dl = turn_left(d[0], d[1])
        sp = (p[0]+dl[0], p[1]+dl[1])
        if sp not in walls and (sp, dl) not in explored:
            l = l.copy()
            l.add(p)
            heappush(h, (c+1001, sp, dl, l))

        dr = turn_right(d[0], d[1])
        sp = (p[0]+dr[0], p[1]+dr[1])
        if sp not in walls and (sp, dr) not in explored:
            l = l.copy()
            l.add(p)
            heappush(h, (c+1001, sp, dr, l))

    return len(result_tiles) + 1

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