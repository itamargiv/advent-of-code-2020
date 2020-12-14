def parse_integers(read_file):
    for line in read_file:
        yield int(line)

def test_parse_integers():
    with open('./inputs/test-0I.txt') as given:
        assert next(parse_integers(given)) == 35
        assert [line for line in parse_integers(given)] == [
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576
        ]

def readlines_batch(read_file, sep = '\n'):
    batch = ''
    for line in read_file:
        if line is sep:
            yield batch
            batch = ''
        else:
            batch += line

    yield batch

def test_readlines_batch():
    with open('./inputs/test-0F.txt') as given:
        assert next(readlines_batch(given)) == 'abc\n', "Cannot read single line"
        assert next(readlines_batch(given)) == 'a\nb\nc\n', "Cannot collect multiple lines"
        assert [batch for batch in readlines_batch(given)] == ['ab\nac\n', 'a\na\na\na\n', 'b'], "Cannot be comprehended into a list"

def strip_lines(read_file):
    for line in read_file:
        yield line.strip()

def test_strip_lines():
    with open('./inputs/test-0C.txt') as given:
        assert next(strip_lines(given)) == '..##.......', "Cannot strip new-lines"
        assert [line for line in strip_lines(given)] == [
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#'
        ], "Cannot be comrehended into a list"

