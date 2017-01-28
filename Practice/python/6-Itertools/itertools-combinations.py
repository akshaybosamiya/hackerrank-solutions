#https://www.hackerrank.com/challenges/itertools-combinations
from itertools import combinations
s,n = input().split()
for j in range(int(n)):
    print(*[''.join(i) for i in combinations(sorted(s),int(j)+1)],sep='\n')