#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
i,j,k=map(int,input().strip().split())
noBeautifulDay = 0
while(i<=j):
    revI=int(str(i)[::-1])
    if(abs(i-revI)%k == 0):
        noBeautifulDay += 1
    i += 1        
print(noBeautifulDay)        