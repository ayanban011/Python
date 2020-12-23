l=[]
a=[]
keyboards=[3,1]
drives=[5,2,8]
for i in range(2):
    for j in range(3):
        l.append(keyboards[i]+drives[j])
for k in range(len(l)):
    if(l[k]<=10):
        a.append(l[k])
print(max(a))
            
