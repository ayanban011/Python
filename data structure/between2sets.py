#!/bin/python3

import os
import sys
from fractions import gcd
from functools import reduce
#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    c=0
    for k in range(1,101):
        f=1
        for i in range(n):
            if(k%a[i]>0):
                f=0
        for j in range(m):
            if(b[j]%k>0):
                f=0
        if(f==1):
            c+=1
    return c
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

