#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min1=scores[0]
    max1=scores[0]
    ca=0
    cb=0
    l=[]
    for i in range(n):
        if(scores[i]>max1):
            max1=scores[i]
            ca+=1
        elif(scores[i]<min1):
            min1=scores[i]
            cb+=1
    l.append(ca)
    l.append(cb)
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

