import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    state = None
    keys = []
    locks = []

    for i, line in enumerate(lines):
        if line and not state:
            if line[0] == '.':
                state = 'key'
                heights = [0]*len(line)

            elif line[0] == '#':
                state = 'lock'
                heights = [0]*len(line)

        if not line:
            if state == 'key':
                keys.append(heights)
            if state == 'lock':
                locks.append(heights)
            state = None
            continue
        
        if state == 'key':
            for j, c in enumerate(line):
                if c == '#':
                    heights[j] += 1
                    
        if state == 'lock':
            for j, c in enumerate(line):
                if c == '#':
                    heights[j] += 1

    if state == 'key':
        keys.append(heights)
    if state == 'lock':
        locks.append(heights)
    state = None

    for k in keys:
        for l in locks:
            for kk, ll in zip(k, l):
                if kk + ll <= 7:
                    continue
                break
            else:
                result += 1

    return result 
                

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        pass

    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution)(file_directory / 'input.txt'))
    if 0: # run part 2
        print('\n----------------part2----------------\n')
        print(benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))