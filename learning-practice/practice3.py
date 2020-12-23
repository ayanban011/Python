def factors(n):
    flist=[]
    for i in range(1,n+1):
        if(n%i==0):
            flist.append(i)
    return(flist)
def isprime(n):
    return(factors(n)==[1,n])
def sumprimes(l):
    pl=[]
    add=0
    for i in range(len(l)):
        if(isprime(l[i])):
            pl.append(l[i])
    for i in range(len(pl)):
        add=add+pl[i]
    return(add)
    
