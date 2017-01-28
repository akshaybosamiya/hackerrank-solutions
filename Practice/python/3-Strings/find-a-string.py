string = input()
substring = input()
count = 0
for i in range(len(string)):
    if(string[i:i+len(substring)] == substring):
        count = count + 1
print(count)
