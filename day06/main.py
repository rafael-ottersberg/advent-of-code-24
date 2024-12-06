import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def turn_right(direction):
    dx, dy = direction
    if direction == (-1,0):
        return (0,1)
    if direction == (0,1):
        return (1,0)
    if direction == (1,0):
        return (0,-1)
    if direction == (0,-1):
        return (-1,0)
    
def getc(pos, lines):
    if (0 <= pos[0] < len(lines)) & (0 <= pos[1] < len(lines[0])):
        return lines[pos[0]][pos[1]]
    else:
        return None
    

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    pos = (0,0)
    direction = (-1, 0)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '^':
                pos = (i,j)

    i = 0
    next_pos = (pos[0] + direction[0], pos[1]+direction[1])
    next_c = getc(next_pos, lines)
    dpos = set()
    while next_c is not None:
        if next_c == "#":
            direction = turn_right(direction)
            next_pos = (pos[0] + direction[0], pos[1]+direction[1])
            next_c = getc(next_pos, lines)
        else:
            pos = next_pos
            next_pos = (pos[0] + direction[0], pos[1]+direction[1])
            next_c = getc(next_pos, lines)
            dpos.add(pos)
            i += 1

    return len(dpos)

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    
    spos = (0,0)
    direction = (-1, 0)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '^':
                spos = (i,j)

    lc = lines.copy()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            lc = lines.copy()
            pos = spos
            direction = (-1, 0)
            if lc[i][j] != "^" and lc[i][j] != "#":
                s = lc[i]
                s = s[:j] + "#" + s[j + 1:]
                lc[i] = s
                # make tour
                next_pos = (pos[0] + direction[0], pos[1]+direction[1])
                next_c = getc(next_pos, lc)
                dpos = set()
                config = set()
                while next_c is not None:
                    if next_c == "#":
                        direction = turn_right(direction)
                        next_pos = (pos[0] + direction[0], pos[1]+direction[1])
                        next_c = getc(next_pos, lc)
                    else:
                        pos = next_pos
                        next_pos = (pos[0] + direction[0], pos[1]+direction[1])
                        next_c = getc(next_pos, lc)
                        dpos.add(pos)

                        if (pos, direction) in config:
                            result += 1
                            break
                        else:
                            config.add((pos, direction))

    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 0: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))