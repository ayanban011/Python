print("1.while loop fibonacci")
print("2.for loop fibonacci")
a=0
b=1
e=0
f=1
m='y'
while(m=='y'):
    ch=int(input("enter your choice :"))
    if(ch==1):
        n=int(input("enter the range of fibonacci series :"))
        i=1
        while(i<=n):
            c=a+b
            a=b
            b=c
            print(c)
            i+=1
    else:
        n=int(input("enter the range of fibonacci series :"))
        for j in range(1,n+1):
            d=e+f
            e=f
            f=d
            print(d)
    print("do you want to continue(y/n)")
    m=input("enter your choice :")
        
