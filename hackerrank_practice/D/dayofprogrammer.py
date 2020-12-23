#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if(year==1800):
        return("12.09."+str(year))
    elif(year==1700):
        return("12.09."+str(year))
    elif(year==1900):
        return("12.09."+str(year))
    if(year==1918):
        return("26.09."+str(year))
    elif(year%400==0):
        return("12.09."+str(year))
    elif(year%100==0):
        return("13.09."+str(year))
    elif(year%4==0):
        return("12.09."+str(year))
    else:
        return("13.09."+str(year))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

