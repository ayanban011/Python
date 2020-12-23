t=int(input())
for i in range(1,t+1):
    n=int(input())
    add=0
    while(n>0):
        r=n%10
        add+=r
        n//=10
    print(add)
