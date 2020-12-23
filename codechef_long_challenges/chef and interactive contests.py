n,r=list(map(int,input().split()))
a=[]
for _ in range(n):
    x=int(input())
    a.append(x)
for j in range(n):
    if(a[j]>=r):
        print("Good boi")
    else:
        print("Bad boi")
