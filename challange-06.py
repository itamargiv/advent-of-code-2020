from functools import reduce
from re import findall

def validate_document(document, keys):
    return all(key in document for key in keys)

def parse_document_part(part):
    kv_pairs = findall(r'(\w+):([#\w\d]+)', part)
    return dict(kv_pairs)


def create_document_processor(keys):
    def process_documents(data, line):
        document = data["document"]

        if line is '\n':
            is_valid = validate_document(document, keys)
            return {
                "document": {},
                "sum": data["sum"] + 1 if is_valid else data["sum"]
            }

        return {
            **data,
            "document": {
                **parse_document_part(line),
                **document
            }
        }
    
    return process_documents

with open('./inputs/input-0D.txt') as f:
    keys = ["byr", "eyr", "iyr", "ecl", "hcl", "hgt", "pid"]
    data = reduce(create_document_processor(keys), f, {
        "document": {},
        "sum": 0
    })
    last = data["document"]

    if last and validate_document(last, keys):
        print(data["sum"] + 1)
    else:
        print(data["sum"])
