# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:50:53 2020

@author: Ayan
"""

def gcd(a,b):
    if(a>b):
        g = a//b
        n = a-g*b
        if(n==0):
            print(b)
            #return b
        else:
            gcd(b,n)
    else:
        g = b//a
        n = b-g*a
        if(n==0):
            print(a)
            #return a
        else:
            gcd(a,n)
res = gcd(1980,1617)
