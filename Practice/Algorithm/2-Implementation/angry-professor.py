#https://www.hackerrank.com/challenges/angry-professor
#!/bin/python3
import sys
t = int(input().strip())
for a0 in range(t):
    n,k = map(int,input().strip().split(' '))
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    noStudent = 0
    for i in range(len(a)):
        if(a[i]<=0):
            noStudent += 1
    if(noStudent>=k):
        print("NO")
    else:
        print("YES")
    
        
