from functools import reduce
from itertools import chain
from json import dumps
from re import findall

def parse_rule(line):
    # Unpack containing bag and it's contents from line
    (_, container), *bags = findall(r'(\d*)\s*(\w+ \w+) bags?[\,\.]?', line)
    return {
        container: {},
        **reduce(lambda graph, bag: {
            **graph,
            bag[1]: { container: int(bag[0]) }
        } if bag[1] != "no other" else graph, bags, {})
    }


def make_tree(graph, line):
    rules = parse_rule(line)

    return {
        **graph,
        **reduce( lambda update, key: { 
            **update,
            key: {
                **graph[key],
                **rules[key]
            } if key in graph else rules[key]
        } , rules, {})
    }

def count_ancestors(node, tree):
    ancestors = []
    count = 0
    
    while tree[node] or len(ancestors[count:]):
        ancestors += [key for key in tree[node] if key not in ancestors]
        node = ancestors[count]
        count += 1

    return count

# Result
with open('./inputs/input-0G.txt') as f:
    tree = reduce(make_tree, f, {})
    print(count_ancestors('shiny gold', tree))

# Tests
with open('./inputs/test-0G.txt') as given:
    tests = [
        (
            parse_rule('light red bags contain 1 bright white bag.'),
            { 
                'light red': {},
                'bright white': { 'light red': 1 } 
            },
            "Cannot parse one bag"
        ),
        (
            parse_rule('light red bags contain 1 bright white bag, 2 muted yellow bags.'),
            { 
                'light red': {},
                'bright white': { 'light red': 1 },
                'muted yellow': { 'light red': 2 } 
            },
            "Cannot parse multiple bags"
        ),
        (
            parse_rule('faded blue bags contain no other bags.'),
            { 
                'faded blue': {}
            },
            "Cannot parse orphaned leaf nodes"
        ),
        (
            reduce(make_tree, [
                'light red bags contain 1 bright white bag.',
                'dark orange bags contain 3 bright white bags.'
            ], {}),
            {
                'light red': {},
                'dark orange': {},
                'bright white': { 
                    'light red': 1,
                    'dark orange': 3 
                }
            },
            "Cannot chart one bag across lines"
        ),
        (
            reduce(make_tree, [
                'light red bags contain 1 bright white bag, 2 muted yellow bags.',
                'dark orange bags contain 3 bright white bags, 4 muted yellow bags.'
            ], {}),
            { 
                'light red': {},
                'dark orange': {},
                'bright white': { 
                    'light red': 1,
                    'dark orange': 3 
                },
                'muted yellow': { 
                    'light red': 2,
                    'dark orange': 4
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
                'vibrant plum': {},
                'faded blue': {
                    'vibrant plum': 5
                },
                'dotted black': {
                    'vibrant plum': 6
                },
            },
            "Cannot chart empty bags across lines"
        ),
        (
            count_ancestors('bright white' ,{
                'dark orange': {},
                'bright white': { 
                    'dark orange': 1
                }
            }),
            1,
            "Cannot count single ancestor"
        ),
        (
            count_ancestors('bright white' ,{
                'dotted black': {},
                'dark orange': {
                    'dotted black': 1
                },
                'bright white': { 
                    'dark orange': 1
                }
            }),
            2,
            "Cannot count ancestor chain"
        ),
        (
            count_ancestors('bright white' ,{
                'dotted black': {},
                'faded blue': {},
                'dark orange': {
                    'dotted black': 1,
                    'faded blue': 1
                },
                'bright white': { 
                    'dark orange': 1
                }
            }),
            3,
            "Cannot count ancestor chain across branches"
        ),
        (
            count_ancestors('bright white' ,{
                'faded blue': {},
                'light gray': {
                    'faded blue': 1
                },
                'dark orange': {
                    'faded blue': 1
                },
                'bright white': { 
                    'dark orange': 1,
                    'light gray': 1
                }
            }),
            3,
            "Cannot dedupe ancestors from chain"
        ),
        (
            count_ancestors('shiny gold', reduce(make_tree, given, {})),
            4,
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


