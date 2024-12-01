import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    left = []
    right = []
    for i, line in enumerate(lines):
        nr1, nr2 = line.split(" ", 1)
        nr1 = int(nr1.strip())
        nr2 = int(nr2.strip())

        left.append(nr1)
        right.append(nr2)

    left.sort()
    right.sort()

    for l, r in zip(left, right):
        result += abs(l-r)


    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    left = []
    right = []
    for i, line in enumerate(lines):
        nr1, nr2 = line.split(" ", 1)
        nr1 = int(nr1.strip())
        nr2 = int(nr2.strip())

        left.append(nr1)
        right.append(nr2)

    for l in left:
        for r in right:
            if l == r:
                result += l


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