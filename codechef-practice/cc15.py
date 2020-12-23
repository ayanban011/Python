countbit=0
countnibble=0
countbyte=0
def roman(n):
    global countbit
    global countnibble
    global countbyte
    if(n<10):
        if((n-1)>=16):
            countbit+=2
            roman(n-17)
        elif((n-1)>=8):
            countbyte+=1
            roman(n-9)
        elif((n-1)>=2):
            countnibble+=1
            roman(n-2)
        elif(n-1>0):
            countbit+=1
    else:
        if((n-1)>=16):
            countbit+=2
            roman(n-17)
        elif((n-1)>=8):
            countbyte+=1
            roman(n-9)
        elif((n-1)>=2):
            countnibble+=1
            roman(n-2)
        elif(n-1>=0):
            countbit+=1
    return countbit, countnibble, countbyte
t=int(input())
for i in range(1,t+1):
    n=int(input())
    if(n==1):
        print(1,0,0)
    else:
        p,q,r=roman(n)
        print(p,q,r)
    countbit-=countbit
    countnibble-=countnibble
    countbyte-=countbyte
