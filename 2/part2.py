import re
lines = open("input.txt","r").readlines()

regex = r"(\d+)-(\d+) (\w): (\w+)$"

validcount = 0
for line in lines:
    (lo, hi, find, pw) = re.search(regex, line).groups()
    ch1 = pw[int(lo) - 1] == find
    ch2 = pw[int(hi) - 1] == find
    if ch1 and ch2: 
        continue
    if ch1 or ch2:
        validcount+=1

print(validcount)
