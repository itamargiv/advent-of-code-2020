from functools import reduce
from read_util import strip_lines

def count_octos(octo_sum, item):
    index, line = item
    position = index * 3
    cursor = position % len(line)
    return octo_sum + 1 if line[cursor] == '#' else octo_sum

with open('./inputs/input-0C.txt') as f:
    print(reduce(count_octos, enumerate(strip_lines(f)), 0))