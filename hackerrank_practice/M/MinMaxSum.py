#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    s=0
    a=0
    for i in range(len(arr)-1):
        s+=arr[i]
    for j in range(1,len(arr)):
        a+=arr[j]
    print(s,a)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

