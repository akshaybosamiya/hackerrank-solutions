#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pCount=0
nCount=0
zCount=0
for i in range(len(arr)):
    if(arr[i]>0):
        pCount+=1
    elif(arr[i]<0):
        nCount+=1
    else:
        zCount+=1
print(str(round(pCount/n,6))+"\n"+str(round(nCount/n,6))+"\n"+str(round(zCount/n,6)))
    
