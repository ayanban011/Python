from tkinter import *
def check():
    print("hello ",e1.get(),e2.get())
master=Tk()
Label(master,text="Enter first name :").grid(row=0)
Label(master,text="Enter last name :").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(master,text="check",command=check)
b1.grid(row=2,column=1)
mainloop()
