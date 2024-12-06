import time

def rotate_direction(x, y):
    if x == 0 and y == -1: # UP
        return 1, 0 # RIGHT
    elif x == 1 and y == 0: #RIGHT
        return 0, 1 # DOWN
    elif x == 0 and y == 1: # DOWN
        return -1, 0 # LEFT
    else: # LEFT
        return 0, -1 # UP

def print_grid(grid):
    for r in grid:
        print(r)

with open('input.txt', 'r') as f:
    grid = [x.strip() for x in f.readlines()]

    position = None
    direction = (0, -1)

    # find starting position
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                position = (x, y)

    visited = set()
    visited.add(position)

    while True:
        next_x = position[0] + direction[0]
        next_y = position[1] + direction[1]
        # break if next step leaves grid
        if not (0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid)):
            break
        
        # check for obstacle
        if grid[next_y][next_x] == '#':
            direction = rotate_direction(direction[0], direction[1])
            continue
        
        # update grid visual
        # grid[position[1]][position[1]] = '.'
        # grid[next_y][next_x] = 'O'

        # move forward
        position = (next_x, next_y)
        visited.add(position)

        # print_grid(grid)
        # print('\r'*len(grid))
        # time.sleep(0.3)

    print(len(visited))