#https://www.hackerrank.com/challenges/designer-pdf-viewer
#!/bin/python3
import sys
h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()
width = len(word)
maxHeight = 0
for i in range(width):
    index = ord(word[i])-97 #For 'a' unicode is 97
    if(maxHeight < h[index]):
        maxHeight = h[index]
print(width*maxHeight)
