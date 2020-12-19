from collections import Counter
from read_util import parse_integers, readlines_sort

def get_permutations(i, n, last):
    nexts = []
    diff = n - last

    while diff <= 3 and i < len(numbers) - 1:
        nexts.append(n)
        i += 1
        n =  numbers[i]
        diff = n - last
    
    return nexts

def find_diff_dist(numbers):
    head = [0] + numbers
    tail = numbers + [numbers[-1] + 3]
    diffs = list(map(lambda last, n: n - last, head, tail))

    print(diffs)
    return Counter(diffs)
    

# Result
# with open('./inputs/input-0J.txt') as f:
#     numbers = readlines_sort(parse_integers(f))
#     dist = find_diff_dist(numbers)

#     print(dist)
#     print(dist[1] * dist[3])

# Tests
with open('./inputs/test-0J.txt') as given:
    numbers = readlines_sort(parse_integers(given))
    
    assert find_diff_dist(numbers) == Counter({
        1: 7,
        3: 5
    }), 'Cannot summerize difference distribution'


with open('./inputs/test-0J_1.txt') as given:
    numbers = readlines_sort(parse_integers(given))
    
    assert find_diff_dist(numbers) == Counter({
        1: 8,
        2: 1,
        3: 4
    }), 'Cannot summerize difference distribution'

with open('./inputs/test-1J.txt') as given:
    numbers = readlines_sort(parse_integers(given))

    assert find_diff_dist(numbers) == Counter({
        1: 22,
        3: 10
    }), 'Cannot summerize difference distribution'
