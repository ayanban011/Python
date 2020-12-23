#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s=0
    for i in range(n):
        s+=bill[i]
    si=s-bill[k]
    sii=si//2
    if(b==sii):
        print("Bon Appetit")
    else:
        print(abs(b-sii))
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

