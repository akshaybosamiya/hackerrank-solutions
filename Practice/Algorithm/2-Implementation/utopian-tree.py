#https://www.hackerrank.com/challenges/utopian-tree
#!/bin/python3
import sys
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    height = 1
    if(n == 0):
        print("1")
    elif(n % 2 == 0):
        for i in range(n//2):
            height *= 2
            height += 1
        print(height)
    elif(n % 2 != 0):
        for i in range(n//2):
            height *= 2
            height += 1
        height *= 2
        print(height)
            
        
