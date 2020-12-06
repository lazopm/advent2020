groups = open("input.txt","r").read().split('\n\n')

print(
    sum(map(lambda g:
        len(set.intersection(*map(set, g.strip().split('\n'))))
    , groups))
)
