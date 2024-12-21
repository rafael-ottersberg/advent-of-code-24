import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

a = 0

def get_value(n,a,b,c):
    if n < 4: return n
    if n == 4: return a
    if n == 5: return b
    if n == 6: return c
    if n == 7: return None

def xor(a, b):
    return a^b

def perform_operation(ip,a,b,c, program):
    inst = int(program[ip])
    op = int(program[ip+1])
    ret = None
    if inst == 0: 
        a = a // 2**get_value(op,a,b,c)
    elif inst == 1: 
        b = b ^ op
    elif inst == 2: 
        b = get_value(op,a,b,c) % 8
    elif inst == 3: 
        if a != 0:
            return op, a, b, c, ret
    elif inst == 4:
        b = b ^ c
    elif inst == 5: 
        ret = get_value(op,a,b,c) % 8
    elif inst == 6:
        b = a // 2**get_value(op,a,b,c)
    elif inst == 7: 
        c = a // 2**get_value(op,a,b,c)

    ip += 2
    return ip, a, b, c, ret


def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    program = [int(n) for n in lines[4].split(': ')[1].split(",")]
    
    print(a)

    ip = 0
    res = ""
    while ip < len(program) - 1:
        if ip==0:
            print(a,b,c)
        ip, a, b, c, r = perform_operation(ip, a,b,c, program)
        if r is not None:
            res += str(r) + ","
    print(a,b,c)
    print(res)
    return res

def solve(ip, a, b, c, program, result, cache):
    if (ip, a, b, c, result) in cache:
        return False
    if ip >= len(program) - 1:
        cache.add((ip,a,b,c,result))
        if result == program:
            return True
        else:
            return False
    
    cache.add((ip, a, b, c, result))
    ip, a, b, c, r = perform_operation(ip, a,b,c, program)
    if r is not None:
        result += str(r)

    return solve(ip, a, b, c, program, result, cache)

def backtrace(program, a):
    if not program:
        return a
    
    result = float('inf')
    p = program[-1]
    for b0 in range(8):
        a0 = a*8 + b0
        b1 = b0^5
        c0 = a0 // (2**b1) 
        b2 = b1 ^ c0
        b3 = b2 ^ 6
        if int(p) == (b3 % 8):
            r = backtrace(program[:-1], a0)
            result = min(result, r)
    
    return result


def solution2(input_file):
    result = []
    lines = open(input_file, 'r').read().splitlines()
    program = ""
    for n in lines[4].split(': ')[1].split(","):
        program += n

    a = 0
    a = backtrace(program, a)

    return a

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        #print(benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        #print(benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(benchmark(solution2)(file_directory / 'input.txt'))
