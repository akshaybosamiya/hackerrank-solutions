n=int(input())
mydict = {}
for line in range(n):
    info = input().split(" ")
    score = list(map(float, info[1:]))
    mydict[info[0]] = sum(score) / float(len(score))
print("%.2f" % round(mydict[input()],2))
