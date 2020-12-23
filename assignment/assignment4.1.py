def mystery(l):
     if l == []:
        print(l)
     else:
        print(l[-1:] + mystery(l[:-1]))
a=[13,23,17,81,15]
mystery(a)
