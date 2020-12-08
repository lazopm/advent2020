lines = open("input.txt","r").readlines()
def process_input(line): 
    parts = line.split(' ')
    return (parts[0], int(parts[1]))
instructions = list(map(process_input, lines))

acc = 0
cur = 0
ran = set()
while cur < len(instructions):
    if cur in ran:
        raise Exception(f'exectued instruction {cur} twice acc value: {acc}')
    ran.add(cur)

    (ins, val) =  instructions[cur]
    if ins == 'nop': 
        cur+=1
    elif ins == 'jmp':
        cur+=val
    elif ins == 'acc':
        acc+=val
        cur+=1
    else:
        raise Exception(f'unknown instruction {ins}')
