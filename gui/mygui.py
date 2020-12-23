import tkinter as tk
def meth():
    print("this is a normal text")
    
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
button=tk.Button(root,text="quit",fg="red",width=25,command=root.destroy)
button.pack(side=tk.LEFT)
userText=tk.Button(frame,text="say hello",command=meth)
userText.pack(side=tk.LEFT)
root.mainloop


