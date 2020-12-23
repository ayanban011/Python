# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:24:10 2020

@author: Ayan
"""

''' 
python3 implementation of above solution'''
import math as mt 

MAX=10000

''' 
Create a boolean array "prime[0..n]" and initialize 
all entries it as true. A value in prime[i] will 
finally be false if i is Not a prime, else true.'''

prime=[True for i in range(MAX+1)] 

def SieveOfErastosthenes(): 
	
	prime[1]=False
	
	for p in range(2,mt.ceil(mt.sqrt(MAX))): 
		#if prime[p] is not changes, then it is a prime 
		
		if prime[p]: 
			#set all multiples of p to non-prime 
			for i in range(2*p,MAX+1,p): 
				prime[i]=False
				
#find the product of 1st N prime numbers 

def solve(n): 
	#count of prime numbers 
	count,num=0,1
	a = []
	#product of prime numbers 
	
	#prod=1
	while count<n: 
		#if the number is prime add it 
		
		if prime[num]: 
			a.append(num) 
			#increase the count 
			count+=1
		num+=1
	return a
SieveOfErastosthenes() 

t = int(input())
for _ in range(t):
    n = int(input())
    a = solve(n)
    b = list(map(int,input().split()))
    for i in range(n):
        if(i>b[i]-1 or i<b[i]-1):
            a[i] = a[b[i]-1]
    for i in range(n):
        print(a[i],end=" ")
    print()
			

    