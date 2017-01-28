arr=list()
n=int(input())
ip=input().split(" ")
for i in range(n):
    arr.append(int(ip[i]))

print(sorted(list(set(arr)))[-2])
"""
arr=list(set(arr))
arr.remove(max(arr))
print(max(arr))

"""


