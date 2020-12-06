import math

lines = open("input.txt","r").readlines()

filled = set()

for line in lines:
    insts = list(line.strip())

    rlo = 0.0
    rhi = 127.0
    for inst in insts[:7]:
        diff = rhi - rlo
        if inst == 'B':
            rlo = rlo + math.ceil(diff/2)
        elif inst == 'F':
            rhi = rlo + math.floor(diff/2)

    clo = 0.0
    chi = 7.0
    for inst in insts[-3:]:
        diff = chi - clo
        if inst == 'R':
            clo = clo + math.ceil(diff/2)
        elif inst == 'L':
            chi = clo + math.floor(diff/2)

    filled.add(int(8 * rlo + clo))

for i in range(127*8+7):
    if i not in filled and i + 1 in filled and i -1 in filled:
        print(i)
        break
