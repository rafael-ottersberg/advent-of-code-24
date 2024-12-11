import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

cache = {}

def solve_number(n, blinks):
    if (n, blinks) in cache:
        return cache[(n, blinks)]
    
    res = 0
    b = blinks - 1
    ns = str(n)

    if blinks == 0:
        res =  1
    
    elif n == 0:
        res = solve_number(1, b)

    elif len(ns) % 2 == 0:
        l = len(ns)
        res = solve_number(int(ns[:l//2]), b) + solve_number(int(ns[l//2:]), b)
    else:
        res = solve_number(n * 2024, b)

    cache[(n, blinks)] = res
    return res

def solution(input_file):
    lines = open(input_file, 'r').read().splitlines()
    numbers = [int(i) for i in lines[0].split(' ')]

    for i in range(25):
        next_numbers = []
        for n in numbers:
            if n == 0:
                next_numbers.append(1)
                continue
            ns = str(n)
            if len(ns) % 2 == 0:
                l = len(ns)
                next_numbers.append(int(ns[:l//2]))
                next_numbers.append(int(ns[l//2:]))
                continue
            next_numbers.append(n * 2024)
        numbers = next_numbers.copy()

    return len(next_numbers)

def solution2(input_file):
    lines = open(input_file, 'r').read().splitlines()
    numbers = [int(i) for i in lines[0].split(' ')]

    result = 0
    for n in numbers:
        result += solve_number(n, 75)

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