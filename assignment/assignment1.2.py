print("1.prime number")
print("2.amstrong number")
print("3.largest number")
m='y'
while(m=='y'):
    ch=int(input("enter your choice"))
    if(ch==1):
        n=int(input())
        j=2
        while(j<n):
            if(n%j==0):
                break
            j+=1
        if(j==n):
            print("yes")
        else:
            print("no")
    elif(ch==2):
        for i in range(1,501):
            order=len(str(i))
            rev=0
            temp=i
            while(temp>0):
                r=temp%10
                rev+=r**order
                temp//=10
            if(rev==i):
                print("amstrong number :",i)
    else:
        a=int(input("enter 1st number"))
        b=int(input("enter 2nd number"))
        c=int(input("enter 3rd number"))
        if(a<b and c<b):
            print("largest number :",b)
        elif(a<c and b<c):
            print("largest number :",c)
        else:
            print("largest number :",a)
    print("do you want to continue(y/n)")
    m=input("enter your choice :") 

        
