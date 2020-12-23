# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 12:31:05 2020

@author: Ayan
"""

t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int,input().split()))
    c.sort(reverse=True)
    b1=0
    b2=0
    b1+=c[0]
    for i in range(1,n):
        if(b1>b2):
            b2+=c[i]
        else:
            b1+=c[i]
    print(max(b1,b2))