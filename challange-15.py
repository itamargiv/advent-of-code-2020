import operator

from json import dumps
from re import match

def parse_command(line):
    (command, sign, integer) = match(r'(\w+) (\+|\-)(\d+)', line).groups()
    return (command, sign, int(integer))

def command_summary(idx, line):
    current = parse_command(line)

    return {
        'command': current,
        'next': get_next_line(idx, current)
    }

def load_program(read_file):
    return [command_summary(idx, line) for (idx, line) in enumerate(read_file)]

def get_next_line(idx, current, goto = 'jmp'):
    ops = {
        '+': operator.add,
        '-': operator.sub
    }

    (command, sign, integer) = current

    return ops[sign](idx, integer) if command == goto else idx + 1

def get_possible_solutions(program):
    idx = 0
    last = 0
    current= {}
    stack = []
    possible_solutions = []
    while idx is not None and idx < len(program):
        current = program[idx]
        stack.append(idx)
        possible_solutions.append({
            "idx": idx,
            "next": get_next_line(idx, current["command"], 'nop')
        })
        last = current["next"]
        idx = last if last not in stack else None

    return possible_solutions

def get_exit_points(program):
    stack_points = [len(program)]
    check_id = 0
    count = 0

    while count < len(stack_points):
        check_id = stack_points[count]
        stack_points += [
            idx for idx, summary in enumerate(program) 
            if summary["next"] == check_id 
            and idx not in stack_points
        ]
        count += 1
        

    return stack_points
        

def analyze(program):
    reverse_stack = get_exit_points(program)
    possible_solutions = get_possible_solutions(program)

    stack = [summary['idx'] for summary in possible_solutions]
    original_summaries = [get_next_line(idx, program[idx]["command"]) for idx in stack]
    exec_point = [idx for idx in original_summaries if idx in reverse_stack]
    
    ids_to_fix = [summary['idx'] for summary in possible_solutions if summary["next"] in reverse_stack or summary["next"] > len(program)]

    return ids_to_fix

# Result
with open('./inputs/input-0H.txt') as f:
    program = load_program(f)

    # This only outputs the line to change
    # TODO: Print out the actual solution
    print(analyze(program))

# Tests
with open('./inputs/test-0H.txt') as given:

    assert get_next_line(0, parse_command('acc +2')) == 1
    assert get_next_line(0, parse_command('nop +0')) == 1
    assert get_next_line(0, parse_command('nop +2')) == 1
    assert get_next_line(0, parse_command('jmp +4')) == 4
    assert get_next_line(2, parse_command('jmp +4')) == 6
    assert get_next_line(6, parse_command('jmp -4')) == 2
    assert get_next_line(0, parse_command('jmp +0')) == 0

    assert dumps(load_program(['acc +1', 'nop +0', 'jmp -2'])) == dumps([
        { 'command': ('acc', '+', 1), 'next': 1 },
        { 'command': ('nop', '+', 0), 'next': 2 },
        { 'command': ('jmp', '-', 2), 'next': 0 }
    ])

    program = load_program(given)
    print(analyze(program))

# def analyze(program):
#     idx = 0
#     call_stack = []
#     current = program[idx]
#     tried = False
#     ops = {
#         '+': operator.add,
#         '-': operator.sub
#     }

#     while current:
#         (command, sign, integer) = current["command"]
#         call_stack.append(idx)
#         last = idx
#         idx = get_next_line(idx, current["command"])
        
#         if idx in call_stack:
#             print(call_stack, idx)

#             if tried: raise Exception(f"Infinite loop from instruction {last + 1}: {current['command']}")

#             print(f"Infinite loop from instruction {last + 1}: {current['command']}, attempting to fix...")
            
#             idx = ops[sign](last, integer) if command == 'nop' else last + 1
#             tried = True
        
#         current = program[idx] if idx < len(program) else False

#     return call_stack

