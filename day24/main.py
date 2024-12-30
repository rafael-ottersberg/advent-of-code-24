import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

def get_value(s, processed_states, calculations):
    if s in processed_states:
        return processed_states[s]
    
    else:
        s1, s2, op = calculations[s]
        match op:
            case 'XOR':
                res = get_value(s1, processed_states, calculations)\
                      ^ get_value(s2, processed_states, calculations)
            
            case 'AND':
                res = get_value(s1, processed_states, calculations)\
                      & get_value(s2, processed_states, calculations)
                
            case 'OR':
                res = get_value(s1, processed_states, calculations)\
                      | get_value(s2, processed_states, calculations)
                
        processed_states[s] = res
        return res

                
def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    part = 1
    processed_states = {}
    calculations = {}
    z_states = []
    for i, line in enumerate(lines):
        if not line:
            part += 1
        elif part == 1:
            state, value = line.split(': ')
            value = int(value)
            processed_states[state] = value
        elif part == 2:
            calc, res = line.split(' -> ')
            s1, op, s2 = calc.split()
            calculations[res] = (s1, s2, op)
            if res.startswith('z'):
                z_states.append(res)
    
    z_states.sort()
    
    for i, s in enumerate(z_states):
        result += get_value(s, processed_states, calculations) * 2**i    

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    part = 1
    processed_states = {}
    calculations = {}
    z_states = []
    for i, line in enumerate(lines):
        if not line:
            part += 1
        elif part == 1:
            state, value = line.split(': ')
            value = int(value)
            processed_states[state] = value
        elif part == 2:
            calc, res = line.split(' -> ')
            s1, op, s2 = calc.split()
            calculations[((s1, s2), op)] = res
            if res.startswith('z'):
                z_states.append(res)
    

    i = 0
    carry = []
    o1 = []
    c1 = []
    c2 = []

    switch_out = set()

    for c in calculations:
        sta, op = c
        res = calculations[c]
        if op == 'XOR' and f"x{i:2d}" in sta and f"y{i:2d}" in sta:
            if res != f"z{i:2d}":
                switch_out.add(res)
                switch_out.add(f"z{i:2d}")

        if op == 'AND' and f"x{i:2d}" in sta and f"y{i:2d}" in sta:
            carry.append(res)
                
    o1.append(None)
    c1.append(None)
    c2.append(None)
    
    # bit 1 to 49
    for i in range(1, len(processed_states) // 2):
        for c, res in calculations.items():
            sta, op = c
            if op == 'XOR' and f"x{i:2d}" in sta and f"y{i:2d}" in sta:
                o1.append(res)

        for c, res in calculations.items():
            sta, op = c
            if op == 'AND' and f"x{i:2d}" in sta and f"y{i:2d}" in sta:
                c1.append(res)
        
        for c, res in calculations.items():
            sta, op = c
            l = carry[i-1]
            r = c1
            if op == 'XOR' and (l in sta or r in sta):
                if res == f"z{i:2d}":
                    if l not in sta:
                        switch_out.add(l)
                        switch_out.add((sta ^ {r}).iterator.next())
                    if r not in sta:
                        switch_out.add(r)
                        switch_out.add((sta ^ {l}).iterator.next())

                else:
                    if l in sta and r in sta:
                        switch_out.add(f'z{i:2d}')
                        switch_out.add(res)

        for c, res in calculations.items():
            sta, op = c
            l = carry[i-1]
            r = c1
            if op == 'AND' and (l in sta or r in sta):
                if res == f"z{i:2d}":
                    if l not in sta:
                        switch_out.add(l)
                        switch_out.add((sta ^ {r}).iterator.next())
                    if r not in sta:
                        switch_out.add(r)
                        switch_out.add((sta ^ {l}).iterator.next())

                else:
                    if l in sta and r in sta:
                        switch_out.add(f'z{i:2d}')
                        switch_out.add(res)
            

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