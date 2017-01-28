#https://www.hackerrank.com/challenges/strange-advertising
n = int(input())
noLike = 0
initNo = 5
while(n>0):
    noLike += (initNo//2)
    initNo = (initNo//2) * 3
    n -= 1
print(noLike)
