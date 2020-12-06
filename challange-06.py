from functools import reduce
from re import findall
from read_util import readlines_batch

def validate_document(document, keys):
    return all(key in document for key in keys)

def parse_document(part):
    kv_pairs = findall(r'(\w+):([#\w\d]+)', part)
    return dict(kv_pairs)


def create_document_processor(keys):
    def process_documents(count, batch):
        document = parse_document(batch)
        is_valid = validate_document(document, keys)
        return count + 1 if is_valid else count
    
    return process_documents

with open('./inputs/input-0D.txt') as f:
    keys = ["byr", "eyr", "iyr", "ecl", "hcl", "hgt", "pid"]
    
    print(reduce(
        create_document_processor(keys), 
        readlines_batch(f), 
        0
    ))

