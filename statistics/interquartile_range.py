n= int(input())
x = list(map(int,input().split()))
f = list(map(int,input().split()))
l= []
l1=[]
for i in range(n):
    for j in range(f[i]):
        l.append(x[i])
l1=sorted(l)
if(n%2>0):
    avg=(l1[(len(l1)+1)//4-1]+l1[(len(l1)+1)//4])/2
    avg1=(l1[(len(l1)+1)*3//4-1]+l1[(len(l1)+1)//4*3])/2
    r=avg1-avg
else:
    avg=(l1[len(l1)//4-1]+l1[len(l1)//4])/2
    avg1=(l1[len(l1)*3//4-1]+l1[len(l1)//4*3])/2
    r=avg1-avg   
print(round(r,2)
