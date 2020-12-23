from tkinter import *
def odd():
    z=int(e1.get())
    y=int(e2.get())
    
    for i in range(z,y+1):
        if(i%2>0):
            print(i)


master=Tk()
Label(master,text="Enter first number :").grid(row=0)
Label(master,text="Enter last number :").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b2=Button(master,text="odd",command=odd)
b2.grid(row=3,column=1)




mainloop()
