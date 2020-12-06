def readlines_batch(read_file, sep = '\n'):
    batch = ''
    
    for line in read_file:
        if line is sep:
            yield batch
        
        batch += line

    yield batch

with open('./inputs/test-0F.txt') as given:
    
    assert next(readlines_batch(given)) == 'abc\n', "Cannot read single line"
    assert next(readlines_batch(given)) == 'a\nb\nc\n', "Cannot collect multiple lines"