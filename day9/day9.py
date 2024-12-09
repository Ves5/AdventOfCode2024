with open('input.txt', 'r') as f:
    disk_map = f.readline().strip()

    uncompact = []
    file = True
    index = 0
    for i in range(len(disk_map)):
        if file:
            uncompact += [index] * int(disk_map[i])
            index += 1
        else:
            uncompact += [-1] * int(disk_map[i])
        file = not file
    # print(uncompact)

    last_swapped_block = len(uncompact) - 1
    for i in range(len(uncompact)):
        if i >= last_swapped_block:
            break
        if uncompact[i] == -1:
            # swap last file block with empty place
            for j in range(last_swapped_block, 0, -1):
                if uncompact[j] != -1:
                    last_swapped_block = j
                    break
            uncompact[i] = uncompact[last_swapped_block]
            uncompact[last_swapped_block] = -1
    # print(uncompact)

    checksum = 0
    i = 0
    while uncompact[i] != -1:
        checksum += i * uncompact[i]
        i += 1
    
    print(checksum)