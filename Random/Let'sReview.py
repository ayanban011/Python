t=int(input())
l=[]
a=[]
for i in range(t):
    s=input()
    for j in range(len(s)):
        if(j%2==0):
            l.append(s[j])
        else:
            a.append(s[j])
    print(''.join(l),''.join(a))
    l.clear()
    a.clear()
