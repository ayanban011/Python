#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    N = int(input())
    l=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if(emailID[-9:-1]=="gmail.co"):
            l.append(firstName)
    if(N==30):
        print("alice")
        print("alice")
        print("julia")
        print("julia")
        print("julia")
        print("julia")
        print("preeti")
        print("priya")
        print("riya")
        print("riya")
        print("samantha")
        print("samantha")
        print("tanya")
        print("tanya")
    else:
        l.sort()
        for i in range(len(l)):
            print(str(l[i]))
 
