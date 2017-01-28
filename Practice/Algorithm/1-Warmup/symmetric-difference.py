m=int(input())
m=set(map(int,input().split()))
n=int(input())
n=set(map(int,input().split()))
a=(m.union(n)).difference(m.intersection(n))
a=list(a)
for i in sorted(a):
    print(i)
