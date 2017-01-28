#https://www.hackerrank.com/challenges/py-the-captains-room
n = int(input())
arr = list(map(int,input().split()))
s = set(arr)
print(((sum(s)*n)-sum(arr))//(n-1)) #Impoertant