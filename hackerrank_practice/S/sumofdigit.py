# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:06:04 2020

@author: Ayan
"""

def sod(n):
    s=0
    while(n>0):
        s+=n%10
        n=n//10
    print(s)
sod(1234)