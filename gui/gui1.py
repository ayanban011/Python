import tkinter as tk
root=tk.Tk()
logo=tk.PhotoImage(file="MY FLAG.gif")
w=tk.Label(root,image=logo).pack(side="right")
expl="only gif is supported"
w2=tk.Label(root,text=expl).pack(side="left")
root.mainloop()
