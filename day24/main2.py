import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *
    
def get_value2(s, processed_states, calculations):
    if s in processed_states:
        return s
    
    else:
        s1, s2, op = calculations[s]
        match op:
            case 'XOR':
                res = (get_value2(s1, processed_states, calculations),
                       get_value2(s2, processed_states, calculations))
            
            case 'AND':
                res = (get_value2(s1, processed_states, calculations),
                       get_value2(s2, processed_states, calculations))
                
            case 'OR':
                res = (get_value2(s1, processed_states, calculations),
                       get_value2(s2, processed_states, calculations))
                
        processed_states[s] = res
        return res


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
            calculations[res] = (s1, s2, op)
            if res.startswith('z'):
                z_states.append(res)
    
    z_states.sort()

    history = {}
    
    for i, s in enumerate(z_states):
        history[s] = get_value2(s, processed_states, calculations)

    for i in range(50):
        print(history[f'z{i:2d}'])
            

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        #print(benchmark(solution2)(file_directory / 'test.txt'))
        #print('\n*******************************\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))