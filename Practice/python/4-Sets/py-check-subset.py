#https://www.hackerrank.com/challenges/py-check-subset
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print(A<B) # < indicate that A is subset of B or not