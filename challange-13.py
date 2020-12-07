from functools import reduce
from itertools import chain
from json import dumps
from re import findall

def parse_rule(line):
    # Unpack containing bag and it's contents from line
    (_, container), *bags = findall(r'(\d*)\s*(\w+ \w+) bags?[\,\.]?', line)
    

    return {
        container: dict(
            (bag, int(quantity)) 
            for quantity, bag in bags
            if quantity
        )
    }

def make_tree(graph, line):
    rules = parse_rule(line)

    return {
        **graph,
        **rules
    }

def count_bags(node, tree):
    if node not in tree or not tree[node]: return 1

    return 1 + sum(quantity * count_bags(key, tree) for key, quantity in tree[node].items())


# # Result
with open('./inputs/input-0G.txt') as f:
    tree = reduce(make_tree, f, {})
    print(count_bags('shiny gold', tree) - 1)

# Tests
with open('./inputs/test-1G.txt') as given:
    tests = [
        (
            parse_rule('shiny gold bags contain 2 dark red bags.'),
            { 'shiny gold': { 'dark red': 2 } },
            "Cannot parse one bag"
        ),
        (
            parse_rule('light red bags contain 1 bright white bag, 2 muted yellow bags.'),
            { 'light red': { 
                'bright white': 1,
                'muted yellow': 2 
            } },
            "Cannot parse one bag"
        ),
        (
            parse_rule('dark violet bags contain no other bags.'),
            { 'dark violet': {} },
            "Cannot parse empty bag"
        ),
        (
            reduce(make_tree, [
                'light red bags contain 1 bright white bag.',
                'dark orange bags contain 3 bright white bags.'
            ], {}),
            {
                'light red': { 'bright white': 1 },
                'dark orange': { 'bright white': 3 }
            },
            "Cannot chart one bag across lines"
        ),
        (
            reduce(make_tree, [
                'light red bags contain 1 bright white bag, 2 muted yellow bags.',
                'dark orange bags contain 3 bright white bags, 4 muted yellow bags.'
            ], {}),
            { 
                'light red': {
                    'bright white': 1,
                    'muted yellow': 2
                },
                'dark orange': {
                    'bright white': 3,
                    'muted yellow': 4
                }
            },
            "Cannot chart multiple bags across lines"
        ),
        (
            reduce(make_tree, [
                'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
                'faded blue bags contain no other bags.'
            ], {}),
            { 
                'vibrant plum': {
                    'faded blue': 5,
                    'dotted black': 6
                },
                'faded blue': {},
            },
            "Cannot chart empty bags across lines"
        ),
        (
            count_bags('shiny gold', reduce(make_tree, [
                'shiny gold bags contain 2 dark red bags.'
            ], {})),
            3,
            "Cannot count across chart"
        ),
        (
            count_bags('shiny gold', reduce(make_tree, given, {})),
            127,
            "Incorrect total sum"
        )
    ]

    for actual, expected, message in tests:
        try:
            assert dumps(actual, sort_keys=True) == dumps(expected, sort_keys=True), message
        except AssertionError as e:
            print(e)
            print('Actual: ', actual)
            print('Expected: ', expected)


