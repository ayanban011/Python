t=int(input())
for i in range(1,t+1):
    a,b,c=list(map(int,input().split()))
    if(a+b+c==180):
        print("YES")
    else:
        print("NO")
