x=int(input())
y=int(input())
z=int(input())
n=int(input())
results=[]
for i in range(x+1):
    for j in range(y+1):
        #print(int(j))
        for k in range(z+1):
            if((int(i)+int(j)+int(k)) != n):
                results.append([i,j,k])
print(results)  
                
            