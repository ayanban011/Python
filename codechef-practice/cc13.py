def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
for _ in range(int(input())):
    arr=list(map(int,input().split()))[1:]
    g=arr[0]
    for i in arr[1:]:
        g=gcd(g,i)
    print(*[x//g for x in arr])
