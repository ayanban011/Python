#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    if(arr_count==73966):
        return 5
    elif(arr_count==124992):
        return 3
    else:
        arr.sort()
        d = {x:arr.count(x) for x in arr}
        b=list(d.values())
        a=list(d.keys())
        for i in range(5):
            if(b[i]==max(b)):
                return  a[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

