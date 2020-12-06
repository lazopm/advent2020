groups = open("input.txt","r").read().split('\n\n')

total = 0
for group in groups:
    total += len(set(''.join(group.split())))

print(total)
