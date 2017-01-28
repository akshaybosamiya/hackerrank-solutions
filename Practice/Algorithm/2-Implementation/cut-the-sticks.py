#https://www.hackerrank.com/challenges/cut-the-sticks
#!/bin/python3
import sys
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while(len(arr)!=0):
    sticksCut = len(arr)
    print(sticksCut)
    lengthOfCut = min(arr)
    for i in range(len(arr)):
        arr[i] -= lengthOfCut
    while(0 in arr):
        arr.remove(0)    #remove() only remove first occurence in list
    #print(arr)
    


