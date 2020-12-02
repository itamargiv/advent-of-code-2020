from functools import reduce


def validate(password, char, minim, maxim):
    first = password[minim - 1]
    second = password[maxim - 1]

    return (char is first) ^ (char is second)

def extract_args(line):
    # Split the arguments from the string (without the newline char)
    args = line[:-1].split(" ")
    
    # Extract and typecast min and max
    minim, maxim = map(int, args[0].split("-"))
    
    # Clean the char to check 
    char = args[1][0]
    password = args[2]

    return (password, char, minim, maxim)


def sum_valid(sum, line):
    args = extract_args(line)
    is_valid = validate(*args)

    return sum + 1 if is_valid else sum

with open('./inputs/input-0B.txt') as f:
    print(reduce(sum_valid, f.readlines(), 0))