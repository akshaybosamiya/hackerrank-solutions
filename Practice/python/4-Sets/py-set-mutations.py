#https://www.hackerrank.com/challenges/py-set-mutations
lenA = int(input())
setA = set(map(int,input().split()))
noOp = int(input())
for i in range(noOp):
    choice = input().split()
    setB = set(map(int,input().split()))
    if(choice[0] == 'intersection_update'):
        setA.intersection_update(setB)
    elif(choice[0] == 'update'):
        setA.update(setB)
    elif(choice[0] == 'symmetric_difference_update'):
        setA.symmetric_difference_update(setB)
    elif(choice[0] == 'difference_update'):
        setA.difference_update(setB)
print(sum(setA))
        
