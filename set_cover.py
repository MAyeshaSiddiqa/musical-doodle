
from collections import defaultdict

F = [set(['ant','apple','act']),
     set(['ant','act']),
     set(['ball','box']),
     set(['cat']),
     set(['ant','apple','act','cat'])
    ]

# First prepare a list of all sets where each element appears
D = defaultdict(list)
for y,S in enumerate(F):
    for a in S:
        D[a].append(y)

L=defaultdict(set)        
# Now place sets into an array that tells us which sets have each size
for x,S in enumerate(F):
    L[len(S)].add(x)

E=[] # Keep track of selected sets
# Now loop over each set size
for sz in range(max(len(S) for S in F),0,-1):
    if sz in L:
        P = L[sz] # set of all sets with size = sz
        while len(P):
            x = P.pop()
            E.append(x)
            for a in F[x]:
                for y in D[a]:
                    if y!=x:
                        S2 = F[y]
                        L[len(S2)].remove(y)
                        S2.remove(a)
                        L[len(S2)].add(y)

print E
