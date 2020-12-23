#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    c=0
    r=0
    for i in range(len(s)):
        if(s[i]=='U'):
            c+=1
        if(s[i]=='D'):
            c-=1
        if(c==0 and s[i]=='U'):
            r+=1
    return r
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

