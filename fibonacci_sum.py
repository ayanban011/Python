# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 19:38:14 2021

@author: Ayan
"""

def fibo(n):
    if n<2:
        return 1
    else:
        res = fibo(n-1) + fibo(n-2)
    return res

n=5
sum = 0
for i in range(0, n-1):
    r = fibo(i)
    sum += r
    print(r)

print("Suma", sum)