import time
from datetime import datetime as dt
from tkinter import *
hosts_path = r"C:\Windows\System32\drivers\etc/hosts"
redirect = "127.0.0.1"
website_list = ["youtube.com","www.youtube.com","https://www.youtube.com"]
def blocker():
    while True:
            if dt(dt.now().year,dt.now().month,dt.now().day,int(e1.get())) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,int(e2.get())):
                    with open(hosts_path, 'r+') as file:
                            content = file.read()
                            for website in website_list:
                                    if website in content:
                                            pass
                                    else:
                                            file.write(redirect + " " + website + "\n")
            else:
                    with open(hosts_path,'r+') as file:
                            content = file.readlines()
                            file.seek(0)
                            for line in content:
                                    if not any(website in line for website in website_list):
                                            file.write(line)
                            file.truncate()
            time.sleep(5)
master=Tk()
Label(master,text="Enter first name :").grid(row=0)
Label(master,text="Enter last name :").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(master,text="check",command=blocker)
b1.grid(row=2,column=1)
mainloop()
