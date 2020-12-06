from functools import reduce
from math import prod
from read_util import strip_lines

def create_counter(index, line):
    def count_octos(slope, octo_sum):
        if index % slope[1] != 0:
            return octo_sum
        
        position = int(index * slope[0] / slope[1])
        cursor = position % len(line)

        return octo_sum + 1 if line[cursor] == '#' else octo_sum
    
    return count_octos

def create_sum(slopes):
    def sum_octos(sums, item):
        return list(map(
            create_counter(*item), 
            slopes, 
            sums
        ))

    return sum_octos

with open('./inputs/input-0C.txt') as f:
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    data = reduce(
        create_sum(slopes), 
        enumerate(strip_lines(f)), 
        [0]*len(slopes) # <-- Initial value: a list of 0 the same size as slopes 
    ) 
    print(prod(data))