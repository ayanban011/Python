#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    cn=0
    cp=0
    cz=0
    for i in range(n):
        if(arr[i]<0):
            cn+=1
        elif(arr[i]>0):
            cp+=1
        else:
            cz+=1
    print(cp/n)
    print(cn/n)
    print(cz/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

