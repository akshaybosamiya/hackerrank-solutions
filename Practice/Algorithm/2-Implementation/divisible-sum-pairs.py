#https://www.hackerrank.com/challenges/divisible-sum-pairs
#!/bin/python3
import sys
n,k = map(int,input().strip().split())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
noPair = 0
for i in range(n):
    for j in range(n):
        if(i<j):
            if((a[i]+a[j]) % k == 0):
                noPair += 1
print(noPair)