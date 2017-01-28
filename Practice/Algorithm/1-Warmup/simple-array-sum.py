#!/bin/python3

import sys

n = int(input())
arr = input().split()
sum = 0
for i in range(len(arr)):
    sum = sum + int(arr[i])
print(sum)

