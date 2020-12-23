t=int(input())
for i in range(1,t+1):
    a,b=list(map(int,input().split()))
    print(max(a,b),a+b)
