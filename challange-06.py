from functools import reduce
from re import findall
from read_util import readlines_batch

def validate_keys(keys, document):
    return all(key in document for key in keys)

def parse_document(part):
    kv_pairs = findall(r'(\w+):([#\w\d]+)', part)
    return dict(kv_pairs)

with open('./inputs/input-0D.txt') as f:
    keys = ["byr", "eyr", "iyr", "ecl", "hcl", "hgt", "pid"]

    print(sum(
        validate_keys(keys, parse_document(batch)) 
        for batch in readlines_batch(f)
    ))

