from functools import reduce

def parse_binary(code, zeros, ones):
    binary_str = "".join(map(
        lambda char: '0' if char in zeros else '1' if char in ones else char, 
        code
    )) 

    return int(binary_str, 2)

def highest_id(highest, line):
    part_code = line.strip()
    id = parse_binary(part_code, 'FL', 'BR')
    
    return id if id > highest else highest

with open('./inputs/input-0E.txt') as f:
    print(reduce(highest_id, f, 0))

