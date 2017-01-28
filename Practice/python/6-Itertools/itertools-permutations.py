#https://www.hackerrank.com/challenges/itertools-permutations
from itertools import permutations
string,k = input().split()
#print(string,k)
#print("\n".join(map(str,permutations(sorted(string),int(k)))))
print(*[''.join(i) for i in permutations(sorted(string),int(k))],sep='\n')
