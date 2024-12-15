import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

def move1(d, location, boxes, edge):
    nloc = (location[0] + d[0], location[1] + d[1])
    possible = True
    if nloc in boxes:
        possible, boxes = move1(d, nloc, boxes, edge)

    if nloc in edge:
        possible = False

    # update this box if movement is possible
    if possible:
        if location in boxes:
            boxes.remove(location)
            boxes.add(nloc)
    
    return possible, boxes

def move2(d, location, lboxes, rboxes, edge):
    nloc = (location[0] + d[0], location[1] + d[1])
    possible = True

    # check if box moves vertically
    if d[0] != 0:
        lb = lboxes.copy()
        rb = rboxes.copy()

        if nloc in lboxes:
            possible, lb, rb = move2(d, nloc, lb, rb, edge)
            # if first half worked check second half
            if possible:
                nloc2 = (nloc[0], nloc[1]+1)
                possible, lb, rb = move2(d, nloc2, lb, rb, edge)

        if nloc in rboxes:
            possible, lb, rb = move2(d, nloc, lb, rb, edge)
            if possible:
                nloc2 = (nloc[0], nloc[1]-1)
                possible, lb, rb = move2(d, nloc2, lb, rb, edge)
        
        if possible:
            #update boxes if both sides worked
            lboxes = lb
            rboxes = rb

    # normal operation for horizontal movement
    else:
        if nloc in lboxes or nloc in rboxes:
            possible, lboxes, rboxes = move2(d, nloc, lboxes, rboxes, edge)

    if nloc in edge:
        possible = False

    # update this box if movement is possible
    if possible:
        if location in lboxes:
            lboxes.remove(location)
            lboxes.add(nloc)

        if location in rboxes:
            rboxes.remove(location)
            rboxes.add(nloc)
    
    return possible, lboxes, rboxes

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    grid = []
    instructions = []
    state = 0
    for i, line in enumerate(lines):
        if not line:
            state += 1
            continue
        if not state:
            grid.append(line)
        else:
            instructions.append(line)

    edge = set()
    boxes = set()
    robot = (0,0)
    
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "#":
                edge.add((i,j))
            elif c == "O":
                boxes.add((i,j))
            elif c == "@":
                robot = (i,j) 

    int_dir = {
        '>': (0,1),
        '<': (0,-1),
        '^': (-1,0),
        'v': (1,0),
    }

    n = 0
    for iline in instructions:
        for inst in iline:
            d = int_dir[inst]

            possible, boxes = move1(d, robot, boxes, edge)
            if possible:
                robot = (robot[0] + d[0], robot[1] + d[1])

            if False:
                print(f"{n}: {inst}")
                n+=1
                for i, line in enumerate(grid):
                    l = ""
                    for j, c in enumerate(line):
                        if (i,j) == robot:
                            l+="@"
                        elif (i,j) in boxes:
                            l+="O"
                        elif (i,j) in edge:
                            l+="#"
                        else:
                            l+="."
                    print(l)

    for b in boxes:
        result += 100*b[0]+b[1]

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    grid = []
    instructions = []
    state = 0
    for i, line in enumerate(lines):
        if not line:
            state += 1
            continue
        if not state:
            grid.append(line)
        else:
            instructions.append(line)

    edge = set()
    lboxes = set()
    rboxes = set()
    robot = (0,0)
    
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "#":
                edge.add((i,2*j))
                edge.add((i,2*j+1))
            elif c == "O":
                lboxes.add((i,2*j))
                rboxes.add((i,2*j+1))
            elif c == "@":
                robot = (i,2*j) 

    int_dir = {
        '>': (0,1),
        '<': (0,-1),
        '^': (-1,0),
        'v': (1,0),
    }

    n = 0
    for iline in instructions:
        for inst in iline:
            d = int_dir[inst]

            possible, lboxes, rboxes = move2(d, robot, lboxes, rboxes, edge)
            if possible:
                robot = (robot[0] + d[0], robot[1] + d[1])

            if False:
                print(f"{n}: {inst}")
                n+=1
                for i, line in enumerate(grid):
                    l = ""
                    for j in range(len(line)*2):
                        if (i,j) == robot:
                            l+="@"
                        elif (i,j) in lboxes:
                            l+="["
                        elif (i,j) in rboxes:
                            l+="]"
                        elif (i,j) in edge:
                            l+="#"
                        else:
                            l+="."
                    print(l)

    for b in lboxes:
        result += 100*b[0]+b[1]

    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 0: # run part 1
        print(benchmark(solution)(file_directory / 'test1.txt'))
        print('\n*******************************\n')
        print(benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))