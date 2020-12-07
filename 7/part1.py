import re
rules = open("input.txt","r").readlines()

recontent = r"\d+ (\w+ \w+) bags?"
rebag = r"(\w+ \w+) bags contain"

bags = dict()
for rule in rules:
    bag = re.search(rebag, rule).groups()[0]
    contents = map(lambda x: x.groups()[0], re.finditer(recontent, rule))
    for color in contents:
        if color not in bags:
            bags[color] = set()
        bags[color].add(bag)

count = set()
cur = {'shiny gold'}
while len(cur):
    nextcur = set()
    for color in cur:
        if color not in bags:
            continue
        count = count.union(bags[color])
        nextcur = nextcur.union(bags[color])
    cur = nextcur

print(len(count))
