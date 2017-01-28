arr=list()
n=int(input())
s=input().split(" ")
for i in range(0,n):
    arr.append(int(s[i]))
t=tuple(arr)
print(hash(t))