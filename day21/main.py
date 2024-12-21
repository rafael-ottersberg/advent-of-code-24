import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

keys = {
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '0': (3,1),
    'A': (3,2),
}

keys2 = {
    "^": (0,1),
    'A': (0,2),
    "<": (1,0),
    "v": (1,1),
    ">": (1,2),
}

dirs = {
    (-1,0): "^",
    (1,0): "v",
    (0,1): ">",
    (0,-1): "<",
}


key_locations = [keys[c] for c in keys]
key_locations2 = [keys2[c] for c in keys2]

def dist(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

def make_instructions(inst_in, level, lp, cache, cache2):
    if (inst_in, level, lp) in cache:
        return cache[(inst_in, level, lp)]
    if level == 2+20-1:
        return inst_in
    
    if level == 0:
        kys = keys
        ky_l = key_locations
    else:
        kys = keys2
        ky_l = key_locations2
    
    lp = 'A'
    ret_instr = ""
    for c in inst_in:
        if (c, lp, level) in cache2:
            ret_instr += cache2[(c, lp, level)]
            lp = c
            continue

        dx, dy = dist(kys[lp], kys[c])
        signx = 0
        signy = 0
        if dx:
            signx = dx // abs(dx)
        if dy:
            signy = dy // abs(dy)

        c1 = (kys[lp][0] + dx, kys[lp][1])
        c2 = (kys[lp][0], kys[lp][1] + dy)

        inst = ""
        ret = None
        ret2 = None
        if c1 in ky_l:
            for _ in range(abs(dx)):
                inst += dirs[(signx, 0)]
            for _ in range(abs(dy)):
                inst += dirs[(0, signy)]
            inst += 'A'
            
            ret = make_instructions(inst, level+1, lp, cache, cache2)
        
        inst = ""
        if c2 in ky_l:
            for _ in range(abs(dy)):
                inst += dirs[(0, signy)]
            for _ in range(abs(dx)):
                inst += dirs[(signx, 0)]

            inst += 'A'
            
            ret2 = make_instructions(inst, level+1, lp, cache, cache2)

        if ret is None:
            ret = ret2
        if ret2 is not None:
            if len(ret2) < len(ret):
                ret = ret2

        ret_instr += ret
        cache2[(c, lp, level)] = ret
        lp = c

    cache[(inst_in, level, lp)] = ret_instr
    return ret_instr

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    cache = {}
    cache2 = {}
    for i, line in enumerate(lines):
        numbers = line[:3]
        numeric = int(numbers)
        instructions = make_instructions(line, 0, "A", cache, cache2)

        res = len(instructions) * numeric
        print(len(instructions), numeric)
        result += res

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