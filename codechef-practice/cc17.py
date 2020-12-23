t=int(input())
for i in range(1,t+1):
    a,b,n=list(map(int,input().split()))
    x=pow(a,n)
    y=pow(b,n)
    if(x>y):
        print("1")
    elif(x<y):
        print("2")
    else:
        print("0")














        
