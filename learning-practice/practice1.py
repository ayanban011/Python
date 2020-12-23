def count(n):
    i=0
    while(n>0):
        n=n//10
        i+=1
    return(i)
def intreverse(n):
    temp=n
    rev=0
    p=count(temp)
    while(temp>0):
        r=temp%10
        rev=rev+(r*(10**(p-1)))
        p=p-1
        temp=temp//10
    return(rev)
