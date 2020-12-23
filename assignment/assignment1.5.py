l=input("Enter a string: ")
print(len(l))
def reverse(l):
    if len(l) == 0:
        return l
    else:
        return reverse(l[1:]) + l[0]
  
s = "Geeksforgeeks"
  
print ("The original string  is : ",end="")
print (l)
  
print ("The reversed string(using recursion) is : ",end="")
print (reverse(l)) 
