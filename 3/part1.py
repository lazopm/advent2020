lines = open("input.txt","r").readlines()

x = 0
y = 0
trees = 0

while y < len(lines):
    line = lines[y]
    if line[x % (len(line) - 1)] == '#':
        trees += 1
    x += 3
    y += 1

print(trees)
