#https://www.hackerrank.com/challenges/kangaroo
#!/bin/python3
import sys
x1,v1,x2,v2 = map(int,input().strip().split())

if(x2>x1 and v2>=v1):
    print("NO")
elif(x2==x1 and v2==v1):
    print("YES")
elif((x1-x2)%(v2-v1) == 0): #Logic is here
    print("YES")
else:
    print("NO")
