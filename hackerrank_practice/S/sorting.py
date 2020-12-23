#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
c=0
for i in range(n):
    for j in range(i,n-1):
        if(a[i]>a[j+1]):
            c+=1
print("Array is sorted in",c,"swaps.")
print("First Element:",min(a))
print("Last Element:",max(a))
