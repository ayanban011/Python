t=int(input())
for i in range(1,t+1):
    n=int(input())
    if(n%2==0):
        n//=2
        n+=1
        print(n)
    else:
        n+=1
        n//=2
        print(n)
