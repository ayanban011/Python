t=int(input())
for i in range(1,t+1):
    n=input()
    c=0
    for j in range(0,len(n)):
        if(n[j]=='4'):
            c+=1
    print(c)
