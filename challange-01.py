with open('./inputs/input-0A.txt') as f:
    numbers = []
    
    for line in f:
        current = int(line)
        midsum = 2020 - current
        
        for i, lhs in enumerate(numbers):
            for rhs in numbers[i:]:
                if rhs == midsum - lhs:
                    print(f'{lhs} * {rhs} * {current} = {lhs * rhs * current}')
                    exit()

        print(current)
        numbers.append(current)



