from read_util import parse_integers

def create_checksum(n, numbers):
    def checksum(i, x):
        return x != n / 2 and any(x + y == n for y in numbers[i:])

    return checksum

def get_preamble(size, input):
    return [next(input) for _ in range(0, size)] 


def find_outlier(buffer, feed):
    n = next(feed)
    if not n: return None
    checksum = create_checksum(n, buffer) 
    
    return (
        n if not any(checksum(i, x) for (i, x) in enumerate(buffer)) 
        else find_outlier(buffer[1:] + [n], feed)
    )

def get_sum_range(n, feed):
    cont_range = []
    current = 0

    while current != n:
        cont_range.append(next(feed))

        while current > n: 
            cont_range = cont_range[1:]
            current = sum(cont_range)
        
        current = sum(cont_range)

    return cont_range

# Result
with open('./inputs/input-0I.txt') as f:
    feed = parse_integers(f)
    outlier = find_outlier(get_preamble(25, feed), feed)
    f.seek(0)
    cont_range = get_sum_range(outlier, feed)

    print(outlier, cont_range)
    print(sum([min(cont_range), max(cont_range)]))

# Tests
with open('./inputs/test-0I.txt') as given:

    input = (n for n in [0,9,8])
    assert get_preamble(1, input) == [0], 'Cannot read generator'
    assert get_preamble(2, input) == [9,8], 'Cannot read several lines'

    feed = parse_integers(given)
    outlier = find_outlier(get_preamble(5, feed), feed) 
    given.seek(0)
    cont_range = get_sum_range(outlier, feed) 

    assert outlier == 127
    assert cont_range == [15, 25, 47, 40]
    assert sum([min(cont_range), max(cont_range)]) == 62
