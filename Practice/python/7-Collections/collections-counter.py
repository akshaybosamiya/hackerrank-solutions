#https://www.hackerrank.com/challenges/collections-counter
from collections import Counter
noShoes = int(input())
shoesSize = list(map(int, input().split()))
noCustomers = int(input())
earnedMoney = 0
c = Counter(shoesSize)
for i in range(noCustomers):
    size,price = map(int,input().split())
    if(size in c.keys()):
        if(c[size]!=0):
            earnedMoney += price
            c[size] -= 1 #Subtract when shoeSized shoe purchased
print(earnedMoney)