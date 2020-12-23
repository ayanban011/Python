t=int(input())
for i in range(1,t+1):
    trn=int(input())
    tr=[int(x) for x in input().split()]
    drn=int(input())
    dr=[int(x) for x in input().split()]
    tsn=int(input())
    ts=[int(x) for x in input().split()]
    dsn=int(input())
    ds=[int(x) for x in input().split()]
    result=all(elem in tr for elem in ts)
    result1=all(elem in dr for elem in ds)
    if(result and result1):
        print("yes")
    else:
        print("no")
