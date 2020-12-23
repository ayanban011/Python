t=int(input())
for i in range(1,t+1):
    p=int(input())
    x=12
    c=0
    while(x>0):
        a=pow(2,x-1)
        if(p>=a):
            c+=1
            p=p-a
            continue
        x-=1
    print(c)
