import os
import sys
import pathlib
from collections import deque
import time

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

def explore_region(i, j, grid, explored):
    c = (i,j)
    if c in explored:
        return 0, 0, explored, None, None
    
    current = grid[i][j]
    q = deque()
    in_q = set()

    q.append((i,j))
    in_q.add((i,j))

    neighbours = set()

    area = 0
    circum = 0

    while q:
        ci,cj = q.popleft()
        neighbour_count = 0
        explored.add((ci,cj))
        for c in ADJ4:
            ni = c[0]+ci
            nj = c[1]+cj
            if is_on_grid(ni, nj, grid):
                n = grid[ni][nj]
                if n == current:
                    if (ni, nj) not in in_q:
                        q.append((ni, nj))
                        in_q.add((ni, nj))
                    neighbour_count += 1
                else:
                    neighbours.add((ni, nj))
            else:
                neighbours.add((ni, nj))

        area += 1
        circum += 4 - neighbour_count
    
    return area, circum, explored, in_q, neighbours



def walk_around(ci, cj, si, sj, di, dj, sdi, sdj, depth, tiles, neighbours_left):
    turn_count = 0
    if depth == 0:
        while turn_count < 5:
            ni = ci + di
            nj = cj + dj
            if (ni, nj) in tiles:
                break
            else:
                turn_count += 1
                di, dj = turn_right(di, dj)

        if turn_count == 4:
            return 4
        return walk_around(ni, nj, si, sj, di, dj, di, dj, 1, tiles, neighbours_left)

    
    directions = [turn_left(di, dj), (di, dj), turn_right(di, dj), (-di, -dj)]
    for i, d in enumerate(directions):
        di, dj = d
        ni = ci + di
        nj = cj + dj
        new_coor = (ni, nj)
        if new_coor in tiles:
            break
        if new_coor in neighbours_left:
            neighbours_left.remove(new_coor)
            
    match i:
        case 0:
            turn_count += 1
        case 2:
            turn_count += 1
        case 3:
            turn_count += 2
    

    if si == ci and sj == cj and di == sdi and dj == sdj and depth>0:
        if neighbours_left:
            coor = list(neighbours_left)[0]
            for c in [(-1,0), (1,0),(0,1),(0,-1)]:
                ni = c[0] + coor[0]
                nj = c[1] + coor[1]
                if (ni, nj) in tiles:
                    break
            
            ndi, ndj = turn_left(c[0], c[1])

            return turn_count + walk_around(ni, nj, ni, nj, ndi, ndj, ndi, ndj, 0, tiles, neighbours_left)
        else:
            return turn_count

    return turn_count + walk_around(ni, nj, si, sj, di, dj, sdi, sdj, depth+1, tiles, neighbours_left)


def solution(input_file):
    result = 0
    explored = set()
    
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            area, circum, explored, _, _ = explore_region(i,j,lines,explored)
            
            result += area * circum

    return result

def solution2(input_file):
    result = 0
    explored = set()
    
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            area, circum, explored, tiles, neighbours = explore_region(i,j,lines,explored)
            
            if area:
                if area == 1:
                    result += 4
                else:
                    sides = walk_around(i, j, i, j, -1, 0, 0, 0, 0, tiles, neighbours)
                    result += area * sides

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
        print(benchmark(solution2)(file_directory / 'test2.txt'))
        print(benchmark(solution2)(file_directory / 'test3.txt'))
        print('\n*******************************\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))