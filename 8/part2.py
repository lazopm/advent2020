lines = open("input.txt","r").readlines()

def process_input(line): 
    parts = line.split(' ')
    return (parts[0], int(parts[1]))

inputs = list(map(process_input, lines))

def execute(instructions, history=None):
    acc = 0
    cur = 0
    ran = set()
    while cur < len(instructions):
        if cur in ran:
            raise Exception(f'exectued instruction {cur} twice')
        ran.add(cur)
        if history != None:
            history.append(cur)

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
    print(acc)

history = list() 
try:
    execute(inputs, history)
except Exception as err:
    print(err)

while True:
    fixcur = history.pop()
    (inst, val) = inputs[fixcur] 
    if inst == 'jmp' or inst == 'nop':
        instructions = inputs.copy()
        instructions[fixcur] = ('jmp' if inst=='nop' else 'nop', instructions[fixcur][1])
        try:
            execute(instructions)
        except:
            continue
        break
