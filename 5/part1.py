import math

lines = open("input.txt","r").readlines()

highest_id = 0
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
    highest_id = int(max(highest_id, (8 * rlo) + clo))

print(highest_id)
