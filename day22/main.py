import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

from helper import *

def mix_prune(number, number2):
    return (number ^ number2) % 16777216

def next_secret(number):
    number = mix_prune(number, number * 64)
    number = mix_prune(number, number // 32)
    number = mix_prune(number, number * 2048)
    return number


def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    
    for i, line in enumerate(lines):
        number = int(line)
        for j in range(2000):
            number = next_secret(number)
        
        result += number
    
    return result


def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    seller_prices = []
    seller_diffs = []

    for i, line in enumerate(lines):
        number = int(line)
        last_price = 0
        prices = []
        diffs = ""
        for j in range(2000):
            number = next_secret(number)
            price = number % 10
            prices.append(price)
            if j != 0:
                d = price - last_price
                if d >= 0:
                    diffs += f"+{d}"
                else:
                    diffs += str(d)
            last_price = price
        
        seller_prices.append(prices)
        seller_diffs.append(diffs)

    patterns = {}

    for diffs, prices in zip(seller_diffs, seller_prices):
        row = set()
        for i in range(len(diffs) // 2 - 4):
            s = diffs[2*i: 2*(i+4)]

            if s in row:
                continue
            row.add(s)
            
            price = prices[i+4]
            if s in patterns:
                patterns[s] += price
            else:
                patterns[s] = price

    for p in patterns:
        result = max(result, patterns[p])

    return result

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
        print(benchmark(solution2)(file_directory / 'input.txt'))