from functools import reduce

def count_octos(data, line):
    line = line.strip()
    position = data["position"]
    cursor = position % len(line)
    octo_sum = data["sum"] + 1 if line[cursor] is '#' else data["sum"]

    return {
        "sum": octo_sum,
        "position": position + 3
    }

with open('./inputs/input-0C.txt') as f:
    print(reduce(count_octos, f.readlines(), {
        "sum": 0,
        "position": 0
    }))