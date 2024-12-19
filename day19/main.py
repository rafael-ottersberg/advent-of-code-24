import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

def match_pattern(p, blocks, cache):
    if not p:
        return True
    
    if p in cache:
        return cache[p]
    
    for b in blocks:
        if p.startswith(b):
            if match_pattern(p[len(b):], blocks, cache):
                cache[p] = True
                return True
            
    cache[p] = False
    return False

def match_pattern2(p, blocks, cache):
    if not p:
        return 1
    
    if p in cache:
        return cache[p]
    
    comb = 0
    for b in blocks:
        if p.startswith(b):
            c = match_pattern2(p[len(b):], blocks, cache)
            comb += c
            
    cache[p] = comb
    return comb

def solution(input_file):
    result = 0
    blocks = []
    patterns = []
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        if i == 0:
            blocks = line.split(', ')

        if i > 1:
            patterns.append(line)

    cache = {}

    for p in patterns:
        if match_pattern(p, blocks, cache):
            result += 1

    return result

def solution2(input_file):
    result = 0
    blocks = []
    patterns = []
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        if i == 0:
            blocks = line.split(', ')

        if i > 1:
            patterns.append(line)

    cache = {}

    for p in patterns:
        r= match_pattern2(p, blocks, cache)
        result += r

    return result

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