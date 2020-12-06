from functools import reduce
from re import findall, match
from read_util import readlines_batch

def validate_measure(value, units):
    quantity, unit = match(r'(\d+)(\w*)', value).groups()

    return validate_enum(unit, list(units)) and validate_range(quantity, units[unit])

def validate_enum(value, enum):
    return value in enum

def validate_range(value, minmax):
    minim, maxim = minmax
    value = int(value)
    
    return minim <= value and value <= maxim

def validate_pattern(value, pattern):
    return match(pattern, value)

def validate(value, rule):
    return all(globals()[f"validate_{name}"](value, constraint) for name, constraint in rule.items())

def validate_rules(rules, document):
    return all(key in document and validate(document[key], rule) for key, rule in rules.items())

def parse_document(part):
    kv_pairs = findall(r'(\w+):([#\w\d]+)', part)
    return dict(kv_pairs)

with open('./inputs/input-0D.txt') as f:
    rules = {
        "byr": { "range": (1920, 2002) },
        "iyr": { "range": (2010, 2020) },
        "eyr": { "range": (2020, 2030) },
        "hgt": { 
            "measure": {
                "cm": (150, 193),
                "in": (59, 76)
            }
        },
        "hcl": { "pattern": r'^#[0-9a-f]{6}$' },
        "ecl": { "enum": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] },
        "pid": { "pattern": r'^[0-9]{9}$' }
    }

    print(sum(
        validate_rules(rules, parse_document(batch))
        for batch in readlines_batch(f)
    ))
