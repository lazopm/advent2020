import re
rules = open("input.txt","r").readlines()

recontent = r"(\d+) (\w+ \w+) bags?"
rebag = r"(\w+ \w+) bags contain"

bags = dict()
for rule in rules:
    bag = re.search(rebag, rule).groups()[0]
    contents = map(lambda x: (int(x.groups()[0]), x.groups()[1]), re.finditer(recontent, rule))
    if bag not in bags:
        bags[bag] = dict()
    for n, color  in contents:
        bags[bag][color] = n

def count_inner_bags(color):
    count = 0
    if color not in bags:
        return 0
    for k, v in bags[color].items():
        count += v + (v * count_inner_bags(k))
    return count

print(count_inner_bags('shiny gold'))
