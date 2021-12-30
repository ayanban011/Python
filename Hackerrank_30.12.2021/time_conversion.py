#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    a = s[0:2]
    a = int(a)
    if(a<10 and s[-2]=='A'):
        return '0'+str(a)+s[2:-2]
    if(s[-2]=='A' and s[1]=='2'):
        return '00'+s[2:-2]
    elif(s[-2]=='P' and a<12):
        a +=12
    s = str(a)+s[2:-2]
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
