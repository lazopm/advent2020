lines = open("input.txt","r").readlines()

def check_slope(dx,dy):
    x = 0
    y = 0
    trees = 0

    while y < len(lines):
        line = lines[y]
        if line[x % (len(line) - 1)] == '#':
            trees += 1
        x += dx
        y += dy 

    return trees

print(
    check_slope(1, 1) *
    check_slope(3, 1) *
    check_slope(5, 1) *
    check_slope(7, 1) *
    check_slope(1, 2) 
)
