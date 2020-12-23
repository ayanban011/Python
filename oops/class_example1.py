def even(arg1,arg2):
    for i in range(arg1,arg+1):
        if(i%2==0):
            print("even :",i)
def odd(arg1,arg2):
    for i in range(arg1,arg2+1):
        if(i%2>0):
            print("odd",i)
c=input()
if(c=='odd'):
    odd(int(input()),int(input()))
else:
    even(int(input()),int(input()))
