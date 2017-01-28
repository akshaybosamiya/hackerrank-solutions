#https://www.hackerrank.com/challenges/apple-and-orange
#!/bin/python3

import sys
s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
noApples=0
noOranges=0
for i in range(len(apple)):
    if(a+apple[i]>=s and a+apple[i]<=t):
        noApples+=1
print(noApples)        
for i in range(len(orange)):
    if(b+orange[i]>=s and b+orange[i]<=t):
        noOranges+=1        
print(noOranges)