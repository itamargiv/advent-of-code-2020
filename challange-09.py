from functools import reduce

def parse_binary(code, zeros, ones):
    binary_str = "".join(map(
        lambda char: '0' if char in zeros else '1' if char in ones else char, 
        code
    )) 

    return int(binary_str, 2)

def taken_seats(data, line):
    part_code = line.strip()
    id = parse_binary(part_code, 'FL', 'BR')
    
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