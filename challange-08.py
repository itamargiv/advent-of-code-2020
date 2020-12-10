from functools import reduce
from read_util import strip_lines

def parse_binary(code, ones):
    binary_str = "".join(map(
        lambda char: '1' if char in ones else '0', 
        code
    )) 

    return int(binary_str, 2)

with open('./inputs/input-0E.txt') as f:
    print(max(
        parse_binary(line, 'BR') for line in strip_lines(f)
    ))
