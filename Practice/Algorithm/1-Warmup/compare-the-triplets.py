#!/bin/python3

import sys

a = input().split(" ")
b = input().split(" ")
alicePoint = 0
bobPoint = 0
for i in range(len(a)):#can len(b) also
    if(int(a[i]) > int(b[i])):
        alicePoint+=1
    elif(int(a[i]) < int(b[i])):
        bobPoint+=1
print(str(alicePoint)+" "+str(bobPoint))
        
        
