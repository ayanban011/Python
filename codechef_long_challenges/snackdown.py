t=int(input())
count=0
for i in range(1,t+1):
    n,k=list(map(int,input().split()))
    list1=[int(x) for x in input().split()]
    list2=sorted(list1, reverse=True)
    for i in range(len(list2)):
        if(list2[i]>=list2[k-1]):
            count+=1
    print(count)
    count=count-count
