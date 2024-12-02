def isSafe(r):
    safe = True
    for i in range(len(r) - 1):
        level_diff = abs(r[i] - r[i+1])
        if level_diff > 3 or level_diff < 1:
            safe = False
            break
    asc_report = sorted(r)
    desc_report = sorted(r, reverse=True)

    if not (all(i == j for i, j in zip(r, asc_report)) or all(i == j for i, j in zip(r, desc_report))):
        safe = False

    return safe

with open('input.txt', 'r') as f:
    reports = [[int(n) for n in x.strip().split(' ')] for x in f.readlines()]
    
    safe_reports = 0

    for r in reports:
        if isSafe(r):
            safe_reports += 1
    print(safe_reports)

    # part 2
    dampened_safe_reports = 0
    for r in reports:
        if isSafe(r):
            dampened_safe_reports += 1
        else:
            dampened_safe = []
            for n in range(len(r)):
                new_r = r.copy()
                del new_r[n]
                dampened_safe.append(isSafe(new_r))
            if any(dampened_safe):
                dampened_safe_reports += 1
    print(dampened_safe_reports)
                 