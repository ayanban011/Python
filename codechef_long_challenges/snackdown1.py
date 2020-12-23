t=int(input())
flag=0
for j in range(1,t+1):
    n=int(input())
    list1=[int(x) for x in input().split()]
    list2=[int(x) for x in input().split()]
    for i in range(0,len(list1)-2,2):
        list1[i]+=1
        list1[i+1]+=2
        list1[i+2]+=3
    for i in range(len(list1)):
        if(list1[i]==list2[i]):
            flag=1
        else:
            flag=0
    if(flag==1):
        print("TAK")
    else:
        print("NIE")
        
        
