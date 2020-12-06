from functools import reduce
from re import match


def validate(password, char, minim, maxim):
    first = password[minim - 1]
    second = password[maxim - 1]

    return (char is first) ^ (char is second)

def extract_args(line):
    # Extract the arguments from the string
    args = match(r'^(\d+)\-(\d+) (\w): (\w+)\n$', line).groups()
    
    # Unpack args and typecast min and max
    minim, maxim = map(int, args[:2])
    char, password = args[2:]
    
    return (password, char, minim, maxim)


def sum_valid(sum, line):
    args = extract_args(line)
    is_valid = validate(*args)

    return sum + 1 if is_valid else sum

with open('./inputs/input-0B.txt') as f:
    print(reduce(sum_valid, f, 0))