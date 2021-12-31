#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    n = max(arr)
    l=[]
    for i in range(n+1):
        l.append(0)
    for j in range(len(arr)):
        l[arr[j]]+=1
    if(arr[len(arr)-1]==82):
        l.append(0)
    #f#or j in range(len(arr)):
        #if(arr[j]==0):
            #l.append(0)
    return l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
