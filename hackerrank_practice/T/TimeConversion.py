#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    a=int(s[0])
    b=int(s[1])
    c=int(s[3])
    d=int(s[4])
    e=int(s[6])
    f=int(s[7])
    if(s[0]=="1" and s[1]=="2" and s[-2]=="A"):
        a=0
        b=0
        print(a,b,":",c,d,":",e,f,sep="")
    elif(s[0]=="1" and s[1]=="2" and s[-2]=="P"):
        print(s[:len(s)-2])
    elif(s[-2]=="P"):
        a+=1
        b+=2
        print(a,b,":",c,d,":",e,f,sep="")
    else:
        print(s[:len(s)-2])
    #

if __name__ == '__main__':

    s = input()

    timeConversion(s)


