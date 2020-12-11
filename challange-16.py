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

# Result
with open('./inputs/input-0I.txt') as f:
    feed = parse_integers(f)

    print(find_outlier(get_preamble(25, feed), feed))

# Tests
with open('./inputs/test-0I.txt') as given:

    input = (n for n in [0,9,8])
    assert get_preamble(1, input) == [0], 'Cannot read generator'
    assert get_preamble(2, input) == [9,8], 'Cannot read sevearl lines'

    feed = parse_integers(given)

    assert(find_outlier(get_preamble(5, feed), feed)) == 127
