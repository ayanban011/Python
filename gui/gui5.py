from tkinter import *
from math import *
def eveluate(event):
    res.configure(text="result :"+str(eval(entry.get())))
w=Tk()
Label(w,text="Enter your expression :").pack()
entry=Entry(w)
entry.bind("<Return>",eveluate)
entry.pack()
res=Label(w)
res.pack()
w.mainloop()
