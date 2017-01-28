#https://www.hackerrank.com/challenges/iterables-and-iterators
from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
C = list(combinations(letters,k))
F=filter(lambda c: 'a' in c,C)
#print(list(F))
print("{0:.3}".format(len(list(F))/len(C)))