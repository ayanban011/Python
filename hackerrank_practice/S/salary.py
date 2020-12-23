t=int(input())
for i in range(t):
    x,n=list(map(int,input().split()))
    c=n//x
    s=0
    for j in range(1,c+1):
        s+=x*j
    print(s)
        
