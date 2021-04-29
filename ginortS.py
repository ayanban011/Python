# Enter your code here. Read input from STDIN. Print output to STDOUT
ou = []
oe = []
l = []
d = []
s = input()
for i in range(len(s)):
    if(ord(s[i])>=97 and ord(s[i])<=122):
        l.append(s[i])
    elif(ord(s[i])>=65 and ord(s[i])<=90):
        d.append(s[i])
    else:
        if(int(s[i])%2==0):
            oe.append(s[i])
        else:
            ou.append(s[i])
ou.sort()
oe.sort()
l.sort()
d.sort()
for a in range(len(l)):
    print(l[a],end="")
for b in range(len(d)):
    print(d[b],end="")
for c in range(len(ou)):
    print(ou[c],end="")
for e in range(len(oe)):
    print(oe[e],end="")
