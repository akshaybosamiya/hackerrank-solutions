#https://www.hackerrank.com/challenges/camelcase
#!/bin/python3
import sys
s = input().strip()
noWords=0
for i in range(len(s)):
    if(s[i].isupper()):
        noWords+=1
print(noWords+1)   

#Other ways to do it using one line of map()
#print(sum(map(str.isupper, input())) + 1)
