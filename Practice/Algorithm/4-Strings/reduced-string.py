# https://www.hackerrank.com/challenges/reduced-string
inputString = list(input())
i=0
stringLength = len(inputString)
while(i<stringLength-1): # -1 for check within list index
    if(inputString[i] == inputString[i+1]):
            inputString = inputString[:i]+inputString[i+2:] 
            i=0 # To recheck from the begining 'i' assigned to zero , for worst case scenario string may not be reducable
            stringLength = len(inputString)
    else:
        i+=1
        stringLength = len(inputString)
    
if(len(inputString)==0):
    print("Empty String")
else:
    print("".join(inputString))