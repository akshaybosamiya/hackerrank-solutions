#https://www.hackerrank.com/challenges/mini-max-sum
#!/bin/python
import sys
no = list(map(int,input().strip().split(' ')))
arr = list()
for i  in range(len(no)):
    arr.append(sum(no)-no[i]) #Subtract each no from total sum 
print(min(arr),max(arr))

