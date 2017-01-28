#!/bin/python3

import sys
time = input().strip()
period=time[-2:]
hh,mm,ss=time[:-2].split(":")
#print(period)
#print(time)
#print(hh,mm,ss)
if(period=="PM"):
    if(int(hh)!=12):
        hh=int(hh)+12
else:
    if(int(hh)==12):
        hh=int(hh)-12
        hh=str(hh)+'0'
print(str(hh)+":"+mm+":"+ss)    

