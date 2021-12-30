#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max1 = arr
    max1.sort(reverse=True)
    sum_max=0
    for i in range(len(max1)-1):
        sum_max += max1[i]
    arr.sort()
    sum_min=0
    for j in range(len(arr)-1):
        sum_min+=arr[j]
    print(sum_min,sum_max)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
