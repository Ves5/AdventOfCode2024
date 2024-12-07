import functools

@functools.cache
def calculate(n1: int, n2: int, sign: str):
    if sign == '+':
        return n1 + n2
    if sign == '*':
        return n1 * n2
    if sign == '||':
        return int(str(n1) + str(n2))

def sign_permutations(goal: int, numbers: list[int]):
    if len(numbers) == 2:
        result = 0
        if calculate(numbers[0], numbers[1], '+') == goal:
            result += 1
        elif calculate(numbers[0], numbers[1], '*') == goal:
            result += 1
        elif calculate(numbers[0], numbers[1], '||') == goal:
            result += 1
        return result
    else:
        addition = calculate(numbers[0], numbers[1], '+')
        multiplication = calculate(numbers[0], numbers[1], '*')
        concatenate = calculate(numbers[0], numbers[1], '||')
        return sign_permutations(goal, [addition] + numbers[2:]) + sign_permutations(goal, [multiplication] + numbers[2:]) + sign_permutations(goal, [concatenate] + numbers[2:])
    

with open('input.txt', 'r') as f:
    lines = [x.strip().split(" ") for x in f.readlines()]
    
    for l in lines:
        l[0] = l[0].strip(':')
        
    goal_sum = 0
    for l in lines:
        goal = int(l[0])
        numbers = [int(x) for x in l[1:]]
        
        if sign_permutations(goal, numbers) > 0:
            goal_sum += goal
            
    print(goal_sum)
        
    