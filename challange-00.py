with open('./inputs/input-0A.txt') as f:
    numbers = []
    
    for line in f:
        current = int(line)
        
        for number in numbers:
            if number == 2020 - current:
                print(f'{number} * {current} = {number * current}')
                exit()

        print(current)
        numbers.append(current)



