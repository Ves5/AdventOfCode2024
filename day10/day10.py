def BFS(start: list[tuple[int, int]], grid, max_x, max_y) -> set:
    nines = set()
    next = []
    for p in start:
        # get all 4 neighbours
        p_up = (p[0], p[1] - 1)
        if is_in_bounds(p_up, max_x, max_y):
            if grid[p_up[1]][p_up[0]] == 9 and grid[p[1]][p[0]] == 8:
                nines.add(p_up)
            elif grid[p_up[1]][p_up[0]] == grid[p[1]][p[0]] + 1:
                next.append(p_up)
        p_down = (p[0], p[1] + 1)
        if is_in_bounds(p_down, max_x, max_y):
            if grid[p_down[1]][p_down[0]] == 9 and grid[p[1]][p[0]] == 8:
                nines.add(p_down)
            elif grid[p_down[1]][p_down[0]] == grid[p[1]][p[0]] + 1:
                next.append(p_down)
        p_left = (p[0] - 1, p[1])
        if is_in_bounds(p_left, max_x, max_y):
            if grid[p_left[1]][p_left[0]] == 9 and grid[p[1]][p[0]] == 8:
                nines.add(p_left)
            elif grid[p_left[1]][p_left[0]] == grid[p[1]][p[0]] + 1:
                next.append(p_left)
        p_right = (p[0] + 1, p[1])
        if is_in_bounds(p_right, max_x, max_y):
            if grid[p_right[1]][p_right[0]] == 9 and grid[p[1]][p[0]] == 8:
                nines.add(p_right)
            elif grid[p_right[1]][p_right[0]] == grid[p[1]][p[0]] + 1:
                next.append(p_right)
    if len(next) > 0:
        nines |= BFS(next, grid, max_x, max_y)

    return nines
        
def BFS2(start: list[tuple[int, int]], grid, max_x, max_y) -> set:
    nines = []
    next = []
    for p in start:
        # get all 4 neighbours
        p_up = (p[0], p[1] - 1)
        if is_in_bounds(p_up, max_x, max_y):
            if grid[p_up[1]][p_up[0]] == 9 and grid[p[1]][p[0]] == 8:
                nines.append(p_up)
            elif grid[p_up[1]][p_up[0]] == grid[p[1]][p[0]] + 1:
                next.append(p_up)
        p_down = (p[0], p[1] + 1)
        if is_in_bounds(p_down, max_x, max_y):
            if grid[p_down[1]][p_down[0]] == 9 and grid[p[1]][p[0]] == 8:
                nines.append(p_down)
            elif grid[p_down[1]][p_down[0]] == grid[p[1]][p[0]] + 1:
                next.append(p_down)
        p_left = (p[0] - 1, p[1])
        if is_in_bounds(p_left, max_x, max_y):
            if grid[p_left[1]][p_left[0]] == 9 and grid[p[1]][p[0]] == 8:
                nines.append(p_left)
            elif grid[p_left[1]][p_left[0]] == grid[p[1]][p[0]] + 1:
                next.append(p_left)
        p_right = (p[0] + 1, p[1])
        if is_in_bounds(p_right, max_x, max_y):
            if grid[p_right[1]][p_right[0]] == 9 and grid[p[1]][p[0]] == 8:
                nines.append(p_right)
            elif grid[p_right[1]][p_right[0]] == grid[p[1]][p[0]] + 1:
                next.append(p_right)
    if len(next) > 0:
        nines += BFS2(next, grid, max_x, max_y)

    return nines

def is_in_bounds(point, x, y):
    return 0 <= point[0] < x and 0 <= point[1] < y

with open('input.txt', 'r') as f:
    grid = [[int(c) for c in x.strip()] for x in f.readlines()]

    score_sum = 0
    score_trails = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                nines = BFS([(x, y)], grid, len(grid[0]), len(grid))
                score_sum += len(nines)
                nines2 = BFS2([(x, y)], grid, len(grid[0]), len(grid))
                score_trails += len(nines2)
    
    print(score_sum)
    print(score_trails)
