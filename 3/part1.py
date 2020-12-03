lines = open("input.txt","r").readlines()

# Finds repeating patterin in the trees
def find_pattern(line):
    line=line.strip()
    shift = 1;
    while (shift < len(line)): 
        a=line[0:shift*-1]
        b=line[shift:]
        if a==b: 
            return line[0:shift]  
        shift+=1
    return line

x = 0
y = 0
trees = 0

while y < len(lines):
    pattern = find_pattern(lines[y])
    if pattern[x % len(pattern) - 1] == '#':
        trees += 1
    x += 3
    y += 1

print(trees)
