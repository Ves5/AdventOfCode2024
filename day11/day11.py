import functools

@functools.cache
def transform(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        length = len(str(stone))
        return [int(str(stone)[:length//2]), int(str(stone)[length//2:])]
    else:
        return [stone * 2024]

@functools.cache
def recursive_transform(stone, repeats):
    if repeats == 0:
        if len(str(stone)) % 2 == 0:
            return 2
        else:
            return 1
    else:
        if stone == 0:
            return recursive_transform(1, repeats - 1)
        elif len(str(stone)) % 2 == 0:
            left, right = transform(stone)
            return recursive_transform(left, repeats-1) + recursive_transform(right, repeats-1)
        else:
            return recursive_transform(stone * 2024, repeats-1)

with open('input.txt', 'r') as f:
    stones = [int(x) for x in f.readlines()[0].strip().split(" ")]

    stone_count = 0 
    for stone in stones:
        stone_count += recursive_transform(stone, 24)
    
    print(stone_count)

    stone_count = 0 
    for stone in stones:
        stone_count += recursive_transform(stone, 74)
    
    print(stone_count)
    