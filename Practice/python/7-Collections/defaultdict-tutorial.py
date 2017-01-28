#https://www.hackerrank.com/challenges/defaultdict-tutorial
from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())
for i in range(n):
    d[input().strip()].append(i+1)
for i in range(m):
    B = input().strip()
    if(B in d):
        print(" ".join([str(x) for x in d[B]]))
    else:
        print(-1)
    