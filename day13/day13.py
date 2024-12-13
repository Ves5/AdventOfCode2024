import re

with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

    buttons_prizes = []

    token_price = 0

    for i in range(0, len(lines), 4):
        a = [int(x) for x in re.findall(r"[0-9]+", lines[i])]
        b = [int(x) for x in re.findall(r"[0-9]+", lines[i+1])]
        p = [int(x) for x in re.findall(r"[0-9]+", lines[i+2])]
        p2 = [int(x) + 10000000000000 for x in re.findall(r"[0-9]+", lines[i+2])]

        min_token = 9999
        for j in range(1, 101):
            for k in range(1, 101):
                x = a[0] * k + b[0] * (j)
                y = a[1] * k + b[1] * (j)
                if x == p[0] and y == p[1]:
                    tokens = k*3 + (j)
                    min_token = min(min_token, tokens)
        
        if min_token != 9999:
            token_price += min_token
    
    print(token_price)

    # part2 linear programming goes brrr, or something, idk how to code that :)
    
    # it's clearly minimisation problem for 
    # y = 3xa + xb
    # constraints:
    # prize_x = xa*a[0] + xb*b[0]
    # prize_y = xa*a[1] + xb*b[0]
    # or jut maybe calculate xa and xb from this :) since it's just 2 unknowns, fuck me I'm stupid xD