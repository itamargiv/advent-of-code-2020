from functools import reduce
from read_util import strip_lines

def parse_binary(code, ones):
    binary_str = "".join(map(
        lambda char: '1' if char in ones else '0', 
        code
    )) 

    return int(binary_str, 2)

def taken_seats(data, line):
    id = parse_binary(line, 'BR')
    
    data["taken"].add(id)

    return {
        **data,
        "max": max(id, data["max"])
    }

with open('./inputs/input-0E.txt') as f:
    data = reduce(
        taken_seats, 
        strip_lines(f), 
        {
            "max": 0,
            "taken": set()
        }
    )

    last = data["max"]
    first = last - len(data["taken"]) + 1 # <-- All possible seats + available seat 

    print(set(range(first, last)) - data["taken"])