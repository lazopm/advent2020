inputs = list(map(int, open("input.txt","r").readlines()))

# part 1
def find(pre, num_sum):
    comp = set() 
    for n in pre:
        if n in comp:
            return True
        comp.add(num_sum-n)
    return False


pre = inputs[:25]
incorrect = None
for n in inputs[25:]:
    if find(pre, n) == False:
        incorrect = n 
        break
    pre.pop(0)
    pre.append(n)

print(incorrect) 

# part 2
lo = 0
hi = 1
while sum(inputs[lo:hi]) != incorrect:
    if sum(inputs[lo:hi]) < incorrect:
        hi = hi + 1
    else:
        lo = lo + 1
        hi = lo + 1
)
print(max(inputs[lo:hi]) + min(inputs[lo:hi]))
