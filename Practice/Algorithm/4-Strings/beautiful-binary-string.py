#https://www.hackerrank.com/challenges/beautiful-binary-string
#!/bin/python3
import sys
n = int(input().strip())
B = input().strip()
newB=B.replace("010","")
print((len(B)-len(newB.strip()))//3)

"""
basically we want 010 to disappear from the string. it doesn't matter wheather we changed the first bit, second bit or third bit. and after our replacement the string shouldn't have a new pair of "010".

So by replacing the "010" with "" we bacially acheive that. by finding the difference in lenght of 2 strings( the one with 010 and the one without) gives us count of total bits replaced/missing. since each pair has 3 bits. divide by 3 gives us the total replacements required.
"""
