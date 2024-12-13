import os
import sys
import pathlib
import re

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

def vec_max(a, p_left):
    v1 = ((p_left[0] // a[0] + 1))
    v2 = ((p_left[1] // a[1] + 1))
    return min(min(v1, v2), 101)

def explore_option(a, b, p):
    amax = vec_max(a, p)
    bmax = vec_max(b, p)

    min_r = float('inf')
    for nb in range(bmax, 0, -1):
        vbx = nb * b[0]
        vby = nb * b[1]
        for na in range(0, amax):
            vax = na * a[0]
            vay = na * a[1]

            if vax + vbx == p[0] and vay + vby == p[1]:
                min_r = min(3*na + nb, min_r)
            
            if vax + vbx > p[0] or vay + vby > p[1]:
                continue
    return min_r


def solution(input_file):
    result = 0
    text = open(input_file, 'r').read()

    pattern = r"\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)"
    u, v, g = [], [], []
    for res in re.finditer(pattern, text):
        u0, u1, v0, v1, g0, g1 = [int(g) for g in res.groups()]
        u.append((u0, u1))
        v.append((v0, v1))
        g.append((g0, g1))
    

    for uvg in zip(u, v, g):
        res = explore_option(*uvg)
        if res < float('inf'):
            result += res

    return result

def solution2(input_file):
    result = 0
    text = open(input_file, 'r').read()

    pattern = r"\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)"
    u, v, g = [], [], []
    for res in re.finditer(pattern, text):
        u0, u1, v0, v1, g0, g1 = [int(g) for g in res.groups()]
        u.append((u0, u1))
        v.append((v0, v1))
        g.append((g0, g1))
    
    for uvg in zip(u, v, g):
        u, v, p = uvg
        p = (p[0] + 10000000000000, p[1] + 10000000000000)

        b = (p[1]-u[1]/u[0]*p[0])/(v[1]-u[1]/u[0]*v[0])
        a = (p[0]-b*v[0])/u[0]

        if (abs(a-round(a)) < 1e-2) and (abs(b-round(b)) < 1e-2):
            res = a*3+b
            result += round(res)


    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))