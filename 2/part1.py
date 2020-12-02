import re
lines = open("input.txt","r").readlines()

regex = r"(\d+)-(\d+) (\w): (\w+)$"

validcount = 0
for line in lines:
    (lo, hi, find, pw) = re.search(regex, line).groups()
    count = 0
    for char in pw:
        if char == find:
            count+=1

    if count <= int(hi) and count >= int(lo):
        validcount+=1

print(validcount)
