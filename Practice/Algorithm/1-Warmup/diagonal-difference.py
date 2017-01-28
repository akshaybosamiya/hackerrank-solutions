#!/bin/python3

import sys


n = int(input().strip())
a = [input().split(" ") for _ in range(1,n+1)]
d1=0
d2=0
for i in range(n):
    for j in range(n):
        if(i == j):
            d1+=int(a[i][j]) #leftcorner to rightcorner diagonal
            d2+=int(a[i][(n-1)-i]) #rightcorner to rightcorner diagonal
print(abs(d1-d2))