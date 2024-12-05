import typing

class Rule:
    number = None
    before = set()
    after = set()

    def __init__(self, number) -> None:
        self.number = number
    
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
    
    print(rulebook)

    mid_page_sum = 0
    for m in magazines:
        correct = True
        pages = [int(x) for x in m.split(',')]
        try:
            for i in range(len(pages)):
                if any([x in rulebook[pages[i]].after for x in pages[:i]]):
                    correct = False
                    break
                if any([x in rulebook[pages[i]].before for x in pages[i+1:]]):
                    correct = False
                    break
        except Exception as e:
            print(e)
        if correct:
            mid_page_sum += pages[len(pages)//2+1]

    print(mid_page_sum)