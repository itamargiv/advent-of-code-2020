from functools import reduce
from read_util import readlines_batch

def sum_common(sum, batch):
    lines = batch.strip().split('\n')
    unique_chars = reduce(lambda uniq, line: uniq & set(line), lines, set(lines[0])) 

    return sum + len(unique_chars)

# Tests
with open('./inputs/test-0F.txt') as given:

    assert sum_common(0, 'a\n') == 1, "Cannot sum a single char"
    assert sum_common(0, 'ab\n') == 2, "Cannot sum multiple chars"
    assert sum_common(0, 'a\nb\n') == 0, "Cannot discount across lines"
    assert sum_common(0, 'a\nbc\n') == 0, "Cannot discount multiple chars across lines"
    assert sum_common(0, 'a\na\n') == 1, "Cannot dedupe recurring chars"
    assert sum_common(0, 'a\nab\n') == 1, "Cannot dedupe and sum across lines"
    assert sum_common(0, 'ab\nac\n') == 1, "Cannot dedupe and discount across lines"
    assert sum_common(5, 'ab\n') == 7, "Cannot add to given sum"

    actual = reduce(sum_common, readlines_batch(given), 0)
    assert actual == 6, "Incorrect total sum"

# Result
with open('./inputs/input-0F.txt') as f:
    print(reduce(sum_common, readlines_batch(f), 0))
