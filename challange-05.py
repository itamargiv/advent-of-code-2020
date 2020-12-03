from functools import reduce

def count_octos(slope, octo_sum, line, index):
    if index % slope[1] != 0:
        return octo_sum
    
    position = int(index * slope[0] / slope[1])
    cursor = position % len(line)

    return octo_sum + 1 if line[cursor] is '#' else octo_sum

def sum_octos(data, line, slopes):
    index = data["index"]
    sums = map(
        lambda slope, octo_sum: count_octos(slope, octo_sum, line, index),
        slopes,
        data["sums"]
    )

    return {
        "sums": list(sums),
        "index": index + 1
    }

with open('./inputs/input-0C.txt') as f:
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    data = reduce(lambda acc, line: sum_octos(acc, line.strip(), slopes), f.readlines(), {
        "sums": [0, 0, 0, 0, 0],
        "index": 0
    })

    print(data)
    print(reduce(lambda multi, num: multi * num, data["sums"]))