#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = {x:ar.count(x) for x in ar}
    b=list(d.values())
    c=0
    for i in range(len(b)):
        c+=b[i]//2
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

