import tkinter as tk
#declare a global variable
counter=0
def counter_label(label):
    def count():
        global counter
        counter=counter+1
        label.config(text=str(counter))
        label.after(1000,count)
    count()
root=tk.Tk()
root.title("Counter loop")
label=tk.Label(root,fg="green")
label.pack()
#declare a method
counter_label(label)
button=tk.Button(root,text="stop",width=25,command=root.destroy)
button.pack()
root.mainloop()
