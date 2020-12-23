t=int(input())
list2=[]
list3=[]
for i in range(t):
    n=int(input())
    list1=[int(x) for x in input().split()]
    for j in range(n):
        if(list1[j]%2==0):
            list2.append(list1[j])
        else:
            list3.append(list1[j])
    list4=sorted(list2,reverse=False)
    list5=sorted(list3,reverse=True)
    k=len(list4)
    l=len(list5)
    for m in range(l):
        print(list5[m],end=" ",flush=True)
    for n in range(k):
        print(list4[n],end=" ",flush=True)
    print()
    list1.clear()
    list2.clear()
    list3.clear()
    list4.clear()
    list5.clear()
