n=int(input())
x=list(map(int,input().split()))
a=sum(x)/n
s=0
for i in range(n):
    p=(x[i]-a)**2
    s+=p
print(round((s/n)**0.5,1))
