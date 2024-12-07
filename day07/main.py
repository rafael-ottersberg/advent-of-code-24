import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper


def calc(nrs, inter, res, operator):
    global res1
    if not nrs:
        if inter == res:
            return True

    else:
        nr = nrs.pop(0)
        inter1 = inter
        inter2 = inter
        if operator == '+':
            inter1 += nr

            
            a = calc(nrs.copy(), inter1, res, '+')
            b = calc(nrs.copy(), inter1, res, '*')
        
        else:
            inter2 *= nr
            a = calc(nrs.copy(), inter2, res, '+')
            b = calc(nrs.copy(), inter2, res, '*')

        return a or b

def calc2(nrs, inter, res, operator):
    global res1
    if not nrs:
        if inter == res:
            return True

    else:
        nr = nrs.pop(0)
        inter1 = inter
        inter2 = inter
        if operator == '+':
            inter1 += nr

            
            a = calc2(nrs.copy(), inter1, res, '+')
            b = calc2(nrs.copy(), inter1, res, '*')
            c = calc2(nrs.copy(), inter1, res, '||')

        elif operator == '*':
            inter2 *= nr

            
            a = calc2(nrs.copy(), inter2, res, '+')
            b = calc2(nrs.copy(), inter2, res, '*')
            c = calc2(nrs.copy(), inter2, res, '||')
        
        else:
            inter3= int(str(inter) + str(nr))
            a = calc2(nrs.copy(), inter3, res, '+')
            b = calc2(nrs.copy(), inter3, res, '*')
            c = calc2(nrs.copy(), inter3, res, '||')

        return a or b or c


def solution(input_file):
    global res1
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):

        res_nrs = line.split(': ')
        res = int(res_nrs[0])
        nrs = [int(n) for n in res_nrs[1].split(' ')]

        inter = 0

        if calc(nrs, inter, res, '+'):
            result += res

    return result

def solution2(input_file):
    global res1
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):

        res_nrs = line.split(': ')
        res = int(res_nrs[0])
        nrs = [int(n) for n in res_nrs[1].split(' ')]

        inter = 0

        if calc2(nrs, inter, res, '+'):
            result += res

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