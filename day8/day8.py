import itertools
from math import isclose

def line_coefficients(x1, y1, x2, y2):
    a = (y1 - y2)/(x1 - x2)
    b = y1 - a*x1
    return a, b

def calculate_antinodes(a, b, n1, n2):
    if n1[0] == n2[0]: # linear equation: x = constant
        distance = abs(n1[1] - n2[1])
        if n1[1] > n2[1]:
            xf = n1[0]
            yf = n1[1] + distance
            xb = n2[0]
            xb = n2[1] - distance
        else:
            xf = n2[0]
            yf = n2[1] + distance
            xb = n1[0]
            xb = n1[1] - distance
    elif n1[1] == n2[1]: # linear equation: y = constant
        distance = abs(n1[0] - n2[0])
        if n1[0] > n2[0]:
            xf = n1[0] + distance
            yf = n1[1]
            xb = n2[0] - distance
            xb = n2[1]
        else:
            xf = n2[0] + distance
            yf = n2[1]
            xb = n1[0] - distance
            xb = n1[1]
    else:
        distance = abs(n1[0] - n2[0])
        if n1[0] > n2[0]:
            xf = n1[0] + distance
            yf = round(a*xf+b)
            xb = n2[0] - distance
            yb = round(a*xb+b)
        else:
            xf = n2[0] + distance
            yf = round(a*xf+b)
            xb = n1[0] - distance
            yb = round(a*xb+b)
    return (xf, yf), (xb, yb)

def get_antinodes(n1, n2):
    return (n1[0] - (n2[0] - n1[0]), n1[1] - (n2[1] - n1[1])), (n2[0] - (n1[0] - n2[0]), n2[1] - (n1[1] - n2[1]))

def generate_all_antinodes(a, b, max_x, max_y):
    antinodes = set()
    for x in range(max_x):
        antinode = (x, round(a*x+b))
        if is_in_bounds(antinode, max_x, max_y) and isclose(a*x+b, antinode[1], rel_tol=0.001):
            antinodes.add(antinode)
    
    return antinodes
    
def is_in_bounds(node, max_x, max_y):
    return 0 <= node[0] < max_x and 0 <= node[1] < max_y

with open('input.txt', 'r') as f:
    grid = [x.strip() for x in f.readlines()]
    
    frequenies = {}    

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                if grid[y][x] not in frequenies.keys():
                    frequenies[grid[y][x]] = []
                frequenies[grid[y][x]].append((x, y))
    
    antinodes = set()
    antinodes_harmonics = set()
    # print(frequency)
    for freq in frequenies.keys():
        for n1, n2 in itertools.combinations(frequenies[freq], 2):
            a, b = line_coefficients(n1[0], n1[1], n2[0], n2[1])
            an1, an2 = calculate_antinodes(a, b, n1, n2)
            # an1, an2 = get_antinodes(n1, n2)
            if is_in_bounds(an1, len(grid[0]), len(grid)):
                antinodes.add(an1)
            if is_in_bounds(an2, len(grid[0]), len(grid)):
                antinodes.add(an2)
            harmonics = generate_all_antinodes(a, b, len(grid[0]), len(grid))
            antinodes_harmonics |= harmonics
    
    print(len(antinodes))
    print(len(antinodes_harmonics))