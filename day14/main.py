import os
import sys
import pathlib
import re

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

def solution(input_file):
    lines = open(input_file, 'r').read()

    pat = r"[^0-9-]+(\d+)[^0-9-]+(\d+)[^0-9-]+(-*\d+)[^0-9-]+(-*\d+)"
    robots = []

    ul, ur, bl, br = 0,0,0,0

    for match in re.finditer(pat, lines):
        nrs = [int(n) for n in match.groups()]
        px, py, vx, vy = nrs
        robots.append((px, py, vx, vy))

    w =  101
    h = 103

    w2 = w // 2
    h2 = h // 2
    for r in robots:
        px, py, vx, vy = r
        ptx = (px + 100 * vx) % w
        pty = (py + 100 * vy) % h

        if 0 <= ptx < w2 and 0 <= pty < h2:
            ul += 1

        if w2 < ptx < w and 0 <= pty < h2:
            ur += 1

        if 0 <= ptx < w2 and h2 < pty < h:
            bl += 1

        if w2 < ptx < w and h2 < pty < h:
            br += 1

    return ul * ur * bl * br

def solution2(input_file):
    lines = open(input_file, 'r').read()

    pat = r"[^0-9-]+(\d+)[^0-9-]+(\d+)[^0-9-]+(-*\d+)[^0-9-]+(-*\d+)"
    robots = []

    for match in re.finditer(pat, lines):
        nrs = [int(n) for n in match.groups()]
        px, py, vx, vy = nrs
        robots.append((px, py, vx, vy))

    w =  101
    h = 103

    ### print to file to find artefacts with period w and h
    with open('out.txt', 'w') as f:
        for i in range(0,1000):
            f.write("-----------------------------------\n")
            f.write(f"{i}\n")
            rs = set()
            for r in robots:
                px, py, vx, vy = r
                ptx = (px + i * vx) % w
                pty = (py + i * vy) % h

                rs.add((ptx, pty))


            for y in range(h):
                line = ""
                for x in range(w):
                    if (x,y) in rs:
                        line += "#"
                    else:
                        line += " "
                f.write(line+"\n")

    first_artefact_v = 83
    first_artefact_h = 60

    for ii in range(0,1000):
        for jj in range(0, 1000):
            i = first_artefact_v + ii * w
            j = first_artefact_h + jj * h
            if i == j:
                return i

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))