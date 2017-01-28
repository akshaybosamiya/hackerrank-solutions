#https://www.hackerrank.com/challenges/pangrams
sentence = "".join(input().strip().upper().split()) # convert to upper or lower case letter , remove space from inbetween to not to save blank character to the set
setA = set(sentence)
noAlphabet = 26
if(len(setA) == noAlphabet): #AtLeast once every alphabet should be there
    print("pangram")
else:
    print("not pangram")