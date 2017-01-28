#https://www.hackerrank.com/challenges/py-set-difference-operation
noEnglish = int(input())
rollEnglish = set(map(int,input().split()))
noFrench = int(input())
rollFrench = set(map(int,input().split()))
print(len(rollEnglish.difference(rollFrench)))