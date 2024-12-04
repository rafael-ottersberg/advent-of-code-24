import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    for i, line in enumerate(lines):
        for j in range(len(line) - 3):
            letters = line[j] + line[j+1] + line[j+2] + line[j+3]
            if letters == 'XMAS' or letters == 'SAMX':
                result += 1

    for j in range(len(lines[0])):
        for i in range(len(lines) - 3):
            letters = lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]
            if letters == 'XMAS' or letters == 'SAMX':
                result += 1

    for i in range(-200,200):
        for off in range(-200,200):
            try:
                x = [i, i+1, i+2, i+3]
                y = [i+off, i+off+1, i+off+2, i+off+3]

                for xx, yy in zip(x,y):
                    assert xx>=0
                    assert yy>=0
                    
                letters = lines[x[0]][y[0]] + lines[x[1]][y[1]] + lines[x[2]][y[2]] + lines[x[3]][y[3]]

                if letters == 'XMAS' or letters == 'SAMX':
                    result += 1
            except:
                pass

    for i in range(-200,200):
        for off in range(-200,200):
            try:
                x = [i, i+1, i+2, i+3]
                y = [i+off, i+off-1, i+off-2, i+off-3]

                for xx, yy in zip(x,y):
                    assert xx>=0
                    assert yy>=0

                letters = lines[x[0]][y[0]] + lines[x[1]][y[1]] + lines[x[2]][y[2]] + lines[x[3]][y[3]]

                if letters == 'XMAS' or letters == 'SAMX':
                    result += 1
            except:
                pass

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    for i in range(-200,200):
        for off in range(-200,200):
            try:
                x = [i-1, i, i+1]
                y = [i+off-1, i+off, i+off+1]

                for xx, yy in zip(x,y):
                    assert xx>=0
                    assert yy>=0
                    
                letters1 = lines[x[0]][y[0]] + lines[x[1]][y[1]] + lines[x[2]][y[2]]
                letters2 = lines[x[0]][y[2]] + lines[x[1]][y[1]] + lines[x[2]][y[0]]

                if (letters1 == 'MAS' or letters1 == 'SAM') and ((letters2 == 'MAS' or letters2 == 'SAM')):
                    result += 1
            except:
                pass

            
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