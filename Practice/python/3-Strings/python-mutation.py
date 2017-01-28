string = input()
i = input().split(" ")
n=int(i[0])
string = string[:n]+i[1]+string[(n+1):]
print(string)