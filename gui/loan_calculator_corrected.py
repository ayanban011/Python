from tkinter import *
fields=('Annual Rate','Number of Payment','Loan Principle','Remaining Loan')
def monthlly_payment(entries):
    r=(float(entries['Annual Rate'].get())/100)/12
    print("r",r)
    loan=float(entries['Loan Principle'].get())
    remaining_loan=float(entries['Remaining Loan'].get())
    q=(1+r)**n
    monthly=r*((q*loan-remaining_loan)/(q-1))
    monthly=("%8.2f"%monthly).strip()
    entries['Monthly Payment'].delete(0,END)
    entries['Monthly Payment :%f'].insert(0,monthly)
    print("monthly Payment :%f",floaat(monthly))
def final_balance():
    r=(float(entries['Annual Rate'].get())/100)/12
    print("r",r)
    loan=float(entries['Loan Principle'].get())
    n=float(enytries['Number of Payments'].get())
    q=(1+r)**n
    monthly=float(entries['Monthly Payment'].get())
    q=(1+r)**n
    remaining=q*loan-((q-1)/r)*monthly
    remaining=("%8.2f"%remaining).strip()
    entries['Remaining Loan'].delete(0,END)
    entries['Remaining Loan'].insert(0,remaining)
    print("Remaining Loan :%f"%float(remaining))
    
def makeform(root,fields):
    entries={}
    for field in fields:
        row=Frame(root)
        lab=Label(row,width=22,text=field+": ",anchor='w')
        ent=Entry(row)
        ent.insert(0,"0")
        row.pack(side=TOP,fill=X,padx=5,pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT,expand=YES,fill=X)
        entries[field]=ent

root=Tk()
if __name__=='__main__':
    ents=makeform(root,fields)
    root.bind('<return>',(lambda event,e=ents:fetch(e)))
    b1=Button(root,text='final balance',command=(lambda e=ents:final_balance(e)))
    b1.pack(side=LEFT,padx=5,pady=5)
    b2=Button(root,text='Monthly Payment')
    b2.pack(side=LEFT,padx=5,pady=5)
    b3=Button(root,text='QUIT',command=root.destroy)
    b3.pack(side=LEFT,padx=5,pady=5)
root.mainloop()
