from functools import reduce

def parse_binary(code, zero, one):
    return int(code.replace(zero, '0').replace(one, '1'), 2)

def highest_id(highest, line):
    part_code = line.strip()
    row = parse_binary(part_code[:7], 'F', 'B')
    col = parse_binary(part_code[7:], 'L', 'R')
    id = row * 8 + col
    
    return id if id > highest else highest

with open('./inputs/input-0E.txt') as f:
    print(reduce(highest_id, f, 0))