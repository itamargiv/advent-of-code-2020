from collections import Counter
from read_util import parse_integers, readlines_sort

def find_diff_dist(numbers):
    counter = Counter()
    last = numbers[0]
    
    # First difference is always between 0 and first number
    counter[last] = 1
    # Last difference is always 3
    counter[3] = 1

    for n in numbers[1:]:
        diff = n - last
        counter[diff] += 1
        last = n  

    return counter
    

# Result
with open('./inputs/input-0J.txt') as f:
    numbers = readlines_sort(parse_integers(f))
    dist = find_diff_dist(numbers)

    print(dist)
    print(dist[1] * dist[3])

# Tests
with open('./inputs/test-0J.txt') as given:
    numbers = readlines_sort(parse_integers(given))
    
    assert find_diff_dist(numbers) == Counter({
        1: 7,
        3: 5
    }), 'Cannot summerize difference distribution'


with open('./inputs/test-1J.txt') as given:
    numbers = readlines_sort(parse_integers(given))

    assert find_diff_dist(numbers) == Counter({
        1: 22,
        3: 10
    }), 'Cannot summerize difference distribution'
