n=int(input())
a=[int(ai) for ai in input().split()]
b=[int(bi) for bi in input().split()]
s=0
si=0
for i in range(n):
    si+=(a[i]*b[i])
    s+=b[i]
w=si/s
print(round(w,1))
