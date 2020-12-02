from functools import reduce
from re import match


def validate(password, char, minim, maxim):
    count = password.count(char)

    return minim <= count and count <= maxim

def extract_args(line):
    # Extract the arguments from the string
    args = match("^(\d+)\-(\d+) (\w): (\w+)\n$", line).groups()
    
    # Unpack args and typecast min and max
    minim, maxim = map(int, args[:2])
    char, password = args[2:]
    
    return (password, char, minim, maxim)


def sum_valid(sum, line):
    args = extract_args(line)
    is_valid = validate(*args)

    return sum + 1 if is_valid else sum

with open('./inputs/input-0B.txt') as f:
    print(reduce(sum_valid, f.readlines(), 0))