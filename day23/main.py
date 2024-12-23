import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def solution(input_file):
    result = 0
    connections = {}
    pcs =set()
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        pc1, pc2 = line.split('-')
        if pc1 in connections:
            connections[pc1].append(pc2)
        else:
            connections[pc1] = [pc2]
        pcs.add(pc1)
        if pc2 in connections:
            connections[pc2].append(pc1)
        else:
            connections[pc2] = [pc1]
        pcs.add(pc2)

    trios = []

    for pc in pcs:
        for pc2 in connections[pc]:
            for pc3 in connections[pc2]:
                if pc3 in connections[pc]:
                    trio = [pc, pc2, pc3]
                    trio.sort()
                    if trio not in trios:
                        trios.append(trio)
    
    for trio in trios:
        for pc in trio:
            if pc.startswith('t'):
                result += 1
                break

    return result

def solution2(input_file):
    len_n = 0
    largest_n = set()
    connections = {}
    pcs =set()
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        pc1, pc2 = line.split('-')
        if pc1 in connections:
            connections[pc1].add(pc2)
        else:
            connections[pc1] = {pc2}
        pcs.add(pc1)
        if pc2 in connections:
            connections[pc2].add(pc1)
        else:
            connections[pc2] = {pc1}
        pcs.add(pc2)

    for pc in pcs:
        for subset in powerset(connections[pc]):
            largest_net = set(subset)
            print(f'initial {largest_net}')
            for pc2 in subset:
                largest_net = largest_net & connections[pc2]
                print(f'after pc {pc2} with: {connections[pc2]}')
                print(largest_net)
            
            if len(largest_net) > len_n:
                len_n = len(largest_net)
                largest_n = largest_net
    
    net = sorted(list(largest_n))
    print(largest_n)
    return net
    

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 0: # run part 1
        print(benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        #print(benchmark(solution2)(file_directory / 'input.txt'))