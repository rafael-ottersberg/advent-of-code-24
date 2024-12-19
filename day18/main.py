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
       if i >= 1024: #1024
           break
       x, y = [int(n) for n in line.split(',')]
       walls.add((x,y))

    end = (70,70) #70

    h = [(0, (0,0))]
    heapify(h)
    explored = set()

    while h:
        c, p = heappop(h)
        if p == end:
            return c
        
        for d in ADJ4:
            sp = (p[0]+d[0], p[1]+d[1])
            if sp not in explored and sp not in walls and 0<=sp[0]<=end[0] and 0<=sp[1]<=end[1]:
                heappush(h, (c+1, sp))
                explored.add(sp)

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    all_walls = []
    for i, line in enumerate(lines):
       x, y = [int(n) for n in line.split(',')]
       all_walls.append((x,y))

    end = (70,70) #70

    for i in range(2023, len(all_walls)):
        walls = set(all_walls[:i])
        h = [(0, (0,0))]
        heapify(h)
        explored = set()

        while h:
            c, p = heappop(h)
            if p == end:
                break
            
            for d in ADJ4:
                sp = (p[0]+d[0], p[1]+d[1])
                if sp not in explored and sp not in walls and 0<=sp[0]<=end[0] and 0<=sp[1]<=end[1]:
                    heappush(h, (c+1, sp))
                    explored.add(sp)
        else:
            return all_walls[i-1]

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 0: # run part 1
        #print(benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        #print(benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))