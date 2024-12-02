import os
import sys
import pathlib
import numpy as np

pd = pathlib.Path(__file__).parent.parent
sys.path.append(str(pd))

import helper

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        numbers = line.split(" ")
        nrs = []
        for n in numbers:
            nrs.append(int(n))


        na = np.array(nrs)

        di = np.diff(na)
        d2 = -di

        error = 0
        ok = True
        for d in di:
            if 0<d<4:
                continue
            else:
                ok=False

        if ok:
            result +=1

        ok = True
        for d in d2:
            if 0<d<4:
                continue
            else:
                ok=False

        if ok:
            result +=1



    return result

def test_list(li, depth):
    for i in range(1, len(li)):
        d = li[i] - li[i-1]
        if 0<d<4:
            continue
        
        else:
            if depth==0:
                li2 = li.copy()
                li1 = li.copy()
                li2.pop(i-1)
                li1.pop(i)
                return test_list(li1, 1) or test_list(li2, 1)
            else:
                return False

    return True

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        numbers = line.split(" ")
        nrs = []
        for n in numbers:
            nrs.append(int(n))

        na = np.array(nrs)
        nrsmi = list(-na)

        inc = test_list(nrs, 0)
        dec = test_list(nrsmi, 0)

        if inc or dec:
            result += 1

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