#https://www.hackerrank.com/challenges/py-set-intersection-operation
noEnglish = int(input())
rollEnglish = set(map(int,input().split()))
noFrench = int(input())
rollFrench = set(map(int,input().split()))
print(len(rollEnglish.intersection(rollFrench)))