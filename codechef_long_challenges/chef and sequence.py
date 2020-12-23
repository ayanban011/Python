t=int(input())
sum1=0
sum2=0
for i in range(1,t+1):
    n,k=list(map(int,input().split()))
    list1=[int(x) for x in input().split()]
    list2=sorted(list1, reverse=False)
    p=n-k
    for j in range(p):
        sum1+=list2[j]
        sum2+=(list2[j]**2)
    sum1+=k
    sum2+=k
    if(sum2<=sum1):
        print("YES")
    else:
        print("NO")
        

