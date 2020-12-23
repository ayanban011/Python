# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:47:21 2020

@author: Ayan
"""

t = int(input())
for _ in range(t):
    n,y = map(int,input().split())
    s = input()
    i = 0
    j = 0
    c = 0
    ans = 0
    while(i<n and j<n):
        if(s[i]=='M'):
            if(s[j] == 'I'):
                if(i<j):
                    for x in range(i,j):
                        if(s[x]==':'):
                            c+=1
                else:
                    for x in range(j,i):
                        if(s[x]==':'):
                            c+=1                    
                p = y+1-abs(i-j)+c
                if(p>0):
                    ans+=1
                    i+=1
                    j+=1
                    c =0
                elif(p<0):
                    if(j>i):
                        i+=1
                    else:
                        j+=1
            elif(s[j]=='X'):
                i = j
                j+=1
                i+=1
            else:
                j+=1
        else:
            i+=1
    print(ans)