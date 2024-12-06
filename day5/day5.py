import typing

class Rule:
    number = None
    before = None
    after = None

    def __init__(self, number) -> None:
        self.number = number
        self.before = set()
        self.after = set()
    
    def add_before(self, number):
        self.before.add(number)
    
    def add_after(self, number):
        self.after.add(number)

    def __str__(self) -> str:
        return f"{self.number} before: {self.before} after: {self.after}"
    
    def __repr__(self) -> str:
        return f"{self.number} before: {self.before} after: {self.after}"

rulebook: typing.Dict[int, Rule] = {}

with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    separator = lines.index('')

    rules = lines[:separator]
    magazines = lines[separator+1:]

    for r in rules:
        rule = [int(x) for x in r.split('|')]
        if rule[0] not in rulebook.keys():
            rulebook[rule[0]] = Rule(rule[0])
        rulebook[rule[0]].add_before(rule[1])
        if rule[1] not in rulebook.keys():
            rulebook[rule[1]] = Rule(rule[1])
        rulebook[rule[1]].add_after(rule[0])
    
    # print(rulebook)

    incorrect_orders: list[list[int]] = []

    mid_page_sum = 0
    for m in magazines:
        correct = True
        pages = [int(x) for x in m.split(',')]
        for i in range(len(pages)):
            afters = []
            for x in pages[:i]:
                afters.append(x in rulebook[pages[i]].before)
            if any(afters):
                correct = False
                break
            befores = []
            for x in pages[i+1:]:
                befores.append(x in rulebook[pages[i]].after)
            if any(befores):
                correct = False
                break
        if correct:
            mid_page_sum += pages[len(pages)//2]
        else:
            incorrect_orders.append(pages.copy())

    print(mid_page_sum)

    corrected_mid_sum_pages = 0
    for pages in incorrect_orders:
        correct = False
        while not correct:
            for i in range(len(pages)):
                afters = []
                for x in pages[:i]:
                    afters.append(x in rulebook[pages[i]].before)
                    if afters[-1]:
                        x_index = pages.index(x)
                        tmp = pages[i]
                        pages[i] = x
                        pages[x_index] = tmp
                        break
                if len(afters) > 0 and afters[-1]:
                    break
                befores = []
                for x in pages[i+1:]:
                    befores.append(x in rulebook[pages[i]].after)
                    if befores[-1]:
                        x_index = pages.index(x)
                        tmp = pages[i]
                        pages[i] = x
                        pages[x_index] = tmp
                if len(befores) > 0 and befores[-1]:
                    break
            if not (any(afters) or any(befores)):
                correct = True
        corrected_mid_sum_pages += pages[len(pages)//2]
    
    print(corrected_mid_sum_pages)