#!/bin/python3

import sys
n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
"""
for i in range(k):
    a=a[-1:]+a[:-1]    #one-time right circular shift
"""

for a0 in range(q):
    m = int(input().strip())
    print(a[(m-k)%len(a)]) #module approach
