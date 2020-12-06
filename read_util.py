def readlines_batch(read_file, sep = '\n'):
    batch = ''
    for line in read_file:
        if line is sep:
            yield batch
            batch = ''
        else:
            batch += line

    yield batch

with open('./inputs/test-0F.txt') as given:
    
    assert next(readlines_batch(given)) == 'abc\n', "Cannot read single line"
    assert next(readlines_batch(given)) == 'a\nb\nc\n', "Cannot collect multiple lines"
    assert [batch for batch in readlines_batch(given)] == ['ab\nac\n', 'a\na\na\na\n', 'b'], "Cannot be comprehended into a list"