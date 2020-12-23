from tkinter import *
import sqlite3
db=sqlite3.connect("student.db")
c=db.cursor()
def check():
    z=int(e1.get())
    list1=[(z)]
    c.execute("select * from stud_ where id=?",list1)
    result=c.fetchall()
    '''for i in result:
            print(i)'''
    if(result):
        print("record found")
    else:
        print("record not found")
    mydb=sqlite3.connect('student.db')

    for row in mydb.execute('select * from stud_ where id=?',list1):
        print(row)
    
master=Tk()
Label(master,text="Enter ID :").grid(row=0)
e1=Entry(master)
e1.grid(row=0,column=1)
b1=Button(master,text="OK",command=check)
b1.grid(row=2,column=1)
mainloop()
