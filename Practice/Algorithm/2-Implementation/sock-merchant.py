#https://www.hackerrank.com/challenges/sock-merchant
#Reference Link: https://pymotw.com/2/collections/counter.html
#!/bin/python3
import sys
from collections import Counter #To count occurances of elements in list
n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
noPair = 0
for number in set(c):
    noPair += Counter(c)[number]//2 # Pair having 2 scoks
print(noPair)
