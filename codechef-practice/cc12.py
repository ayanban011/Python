t=int(input())
for i in range(1,t+1):
    a,b,c=list(map(int,input().split()))
    if((a>b)and(a<c)):
        print(a)
    elif((b>a)and(b<c)):
        print(b)
    elif((c>a)and(c>b)):
        print(c)
    elif((a>c)and(a<b)):
        print(a)
    elif((b<a)and(b>c)):
        print(b)
    else:
        print(c)
