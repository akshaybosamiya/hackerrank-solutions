arr = list()
n = int(input())
for i in range(0,n):
    s=input().split(" ")
    if(s[0] == 'insert'):
        arr.insert(int(s[1]),int(s[2]))
    elif(s[0] == 'print'):
        print(arr)
    elif(s[0] == 'remove'):
        arr.remove(int(s[1]))
    elif(s[0] == 'append'):
        arr.append(int(s[1]))
    elif(s[0] == 'sort'):
        arr.sort()
    elif(s[0] == 'pop'):
        arr.pop()
    else:
        arr.reverse()
    
    