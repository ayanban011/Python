
n=int(input("Enter how many elements you want to store in array"))
l=[int(x) for x in input().split()]
y=int(input("enter the elements you want to search"))
for i in range(n):
    if(y==l[i]):
        print("record found",i)
