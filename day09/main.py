import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file):
    result = 0
    line = open(input_file, 'r').read()
    e = False
    filesystem = []
    i = 0
    for l in line:
        nl = int(l)
        for _ in range(nl):
            if not e:
                filesystem.append(i)
            else:
                filesystem.append(-1)
        
        if not e:
            e = True
            i+=1
        else:
            e=False

    j = len(filesystem) - 1
    for i in range(len(filesystem)):
        if filesystem[i] == -1:
            while filesystem[j] == -1:
                j -= 1
            if j <= i:
                break
            temp = filesystem[i]
            filesystem[i] = filesystem[j]
            filesystem[j] = temp
        
    for i, f in enumerate(filesystem):
        if f != -1:
            result += i*f
    return result

def solution2(input_file):
    result = 0
    line = open(input_file, 'r').read()
    e = False
    filesystem = []
    i = 0
    for l in line:
        nl = int(l)

        if not e:
            filesystem.append((i, nl))
        else:
            filesystem.append((-1, nl))
        
        if not e:
            e = True
            i+=1
        else:
            e=False

    
    rj = 0
    while rj < len(filesystem):
        j = len(filesystem) - rj - 1
        if filesystem[j][0] == -1:
            rj += 1
            continue
        space = filesystem[j][1]
        for i in range(len(filesystem)):
            if i >= j:
                break
            avail = filesystem[i][1]
            if filesystem[i][0] != -1:
                continue
            if space > avail:
                continue

            filesystem[i] = filesystem[j]
            filesystem[j] = (-1, space)

            if avail > space:
                filesystem.insert(i+1, (-1, avail-space))
            
            break
        rj += 1

    i = 0
    for f in filesystem:
        for _ in range(f[1]):
            if f[0] != -1:
                result += i*f[0]
            i += 1
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