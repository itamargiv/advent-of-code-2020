from functools import reduce

def parse_binary(code, zero, one):
    return int(code.replace(zero, '0').replace(one, '1'), 2)

def taken_seats(data, line):
    part_code = line.strip()
    row = parse_binary(part_code[:7], 'F', 'B')
    col = parse_binary(part_code[7:], 'L', 'R')
    id = row * 8 + col
    
    data["taken"].add(id)

    return {
        **data,
        "min": min(id, data["min"]) if data["min"] != 0 else id,
        "max": max(id, data["max"])
    }

with open('./inputs/input-0E.txt') as f:
    data = reduce(taken_seats, f, {
        "min": 0,
        "max": 0,
        "taken": set()
    })

    print(set(range(data["min"], data["max"])) - data["taken"])