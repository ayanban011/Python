def descending(l):
    flag=0
    if(len(l)==0):
        return(True)
    else:
       for i in range(len(l)):
           for j in range(1,len(l)):
               if(l[i]>=l[j]):
                   flag=1
               else:
                   flag=0
    if(flag==1):
        return(True)
    else:
        return(False)
