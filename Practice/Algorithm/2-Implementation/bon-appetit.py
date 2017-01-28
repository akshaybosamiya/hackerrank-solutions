#https://www.hackerrank.com/challenges/bon-appetit
n,k = map(int, input().split())
costI = [int(costI_tmp) for costI_tmp in input().strip().split()]
bCharged = int(input().strip())
bActual = (sum(costI)-costI[k])//2
if(bCharged - bActual):
    print(bCharged - bActual)
else:
    print("Bon Appetit")
    
