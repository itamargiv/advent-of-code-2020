import operator

from json import dumps
from re import match

def parse_command(line):
    (command, sign, integer) = match(r'(\w+) (\+|\-)(\d+)', line).groups()
    return (command, sign, int(integer))

def load_program(read_file):
    return [{
        'count': 0,
        'command': parse_command(line)
    } for line in read_file]


def execute(program):
    accumulator = 0

    idx = 0
    current = program[idx]

    ops = {
        '+': operator.add,
        '-': operator.sub
    }

    while current:
        (command, sign, integer) = current["command"]
        if current["count"] > 0: return accumulator

        if command == "acc": accumulator = ops[sign](accumulator, integer)
        
        current["count"] += 1
        idx = ops[sign](idx, integer) if command == 'jmp' else idx + 1

        if idx == len(program): return accumulator
        current = program[idx]
        

# Result
with open('./inputs/input-0H.txt') as f:
    print(execute(load_program(f)))

# Tests
with open('./inputs/test-0H.txt') as given:
    assert parse_command('acc +1') == ('acc', '+', 1), "Cannot parse a + line"
    assert parse_command('acc -1') == ('acc', '-', 1), "Cannot parse a - line"
    
    assert dumps(load_program(['acc +1', 'nop +0'])) == dumps([
        { 'count': 0, 'command': ('acc', '+', 1) },
        { 'count': 0, 'command': ('nop', '+', 0) }
    ])

    assert execute(load_program(given)) == 5
