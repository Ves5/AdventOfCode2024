import re

with open('input.txt', 'r') as f:
    lines = [n.strip() for n in f.readlines()]
    
    match_string = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    compiled = re.compile(match_string)

    mul_sum = 0
    for l in lines:
        results = re.findall(compiled, l)
        for r in results:
            parts = str(r).split(',')
            mul_sum += int(parts[0][4:]) * int(parts[-1][:-1])
    print(mul_sum)

    # part 2
    match_string = r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))"
    compiled = re.compile(match_string)

    enabled_mul_sum = 0
    enabled = True
    for l in lines:
        results = re.findall(compiled, l)
        for r in results:
            if r[2] == "don't()":
                enabled = False
            elif r[1] == "do()":
                enabled = True
            else:
                if enabled:
                    parts = str(r[0]).split(',')
                    enabled_mul_sum += int(parts[0][4:]) * int(parts[-1][:-1])
    
    print(enabled_mul_sum)
