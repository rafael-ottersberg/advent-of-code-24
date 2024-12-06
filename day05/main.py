import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    order = {}

    state1 = 1
    for line in lines:
        if line == '':
            state1 = 0
            continue
        if state1:
            nrs = line.split('|')
            k = int(nrs[0])
            v = int(nrs[1])

            if k not in order:
                order[k] = [v]
            else:
                order[k].append(v)
        
        if not state1:
            nrs = [int(n) for n in line.split(',')]

            flag = True
            for i, n in enumerate(nrs):
                if n in order.keys():
                    n_left = nrs[:i]
                    for v in order[n]:
                        if v in n_left:
                            #print(f"br with {n}/{order[n]}")
                            flag = False
                            break
                
                if not flag:
                    break
            
            else:
                result += nrs[(len(nrs)-1)//2]
            
    return result

def moveleft(line, n):
    i = line.index(n)

    new_index = max(0, i-1)
    line = line[:i] + line[i + 1:]
    # Insert the substring at the new position
    line = line[:new_index] + [n] + line[new_index:]

    return line

def orderline(line, order):
    flag = False
    for i, n in enumerate(line):
        if n in order.keys():
            n_left = line[:i]
            for v in order[n]:
                if v in n_left:
                    line = moveleft(line, n)
                    line = orderline(line, order)
                    flag = True
                    break
        if flag:
            break
    return line


def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    order = {}
    bad_lines = []

    state1 = 1
    for line in lines:
        if line == '':
            state1 = 0
            continue
        if state1:
            nrs = line.split('|')
            k = int(nrs[0])
            v = int(nrs[1])

            if k not in order:
                order[k] = [v]
            else:
                order[k].append(v)
        
        if not state1:
            nrs = [int(n) for n in line.split(',')]

            flag = True
            for i, n in enumerate(nrs):
                if n in order.keys():
                    n_left = nrs[:i]
                    for v in order[n]:
                        if v in n_left:
                            #print(f"br with {n}/{order[n]}")
                            flag = False
                            break
                
                if not flag:
                    break
            
            if not flag:
                bad_lines.append(nrs)

    for line in bad_lines:
        line = orderline(line, order)
        #print(line)
        result += line[(len(line)-1)//2]
            
            
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