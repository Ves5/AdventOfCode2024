def find_xmas(matrix, x, y):
    count = 0
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            try:
                word = ""
                for k in range(4):
                    if y+(i*k) < 0 or x+(j*k) < 0:
                        break
                    word += matrix[y+(i*k)][x+(j*k)]
                if word == "XMAS":
                    count += 1
            except:
                continue
    return count

def find_x_mas(matrix, x, y):
    ms_dict = {"M": 0, "S": 0}
    try:
        if x-1 < 0 or y-1<0:
            return 0
        if matrix[y-1][x-1] in ms_dict.keys() and matrix[y-1][x-1] != matrix[y+1][x+1]:
            ms_dict[matrix[y-1][x-1]] += 1
        if matrix[y-1][x+1] in ms_dict.keys() and matrix[y-1][x+1] != matrix[y+1][x-1]:
            ms_dict[matrix[y-1][x+1]] += 1
        if matrix[y+1][x+1] in ms_dict.keys():
            ms_dict[matrix[y+1][x+1]] += 1
        if matrix[y+1][x-1] in ms_dict.keys():
            ms_dict[matrix[y+1][x-1]] += 1
        if ms_dict["M"] == 2 and ms_dict["S"] == 2:
            return 1
        return 0
    except:
        return 0

with open('input.txt', 'r') as f:
    matrix = [x.strip() for x in f.readlines()]
    
    xmas_count = 0
    x_mas_count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 'X':
                xmas_count += find_xmas(matrix, x, y)
            elif matrix[y][x] == 'A':
                x_mas_count += find_x_mas(matrix, x, y)
    
    print(xmas_count)
    print(x_mas_count)