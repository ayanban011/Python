import sqlite3
db=sqlite3.connect("samp.db")
c=db.cursor()
script='''create table web(id integer primary key,name text, phn integer);
insert into web(name,phn) values('ayan','45000');'''
x=int(input("enter user id :"))
list1=[(x)]
c.execute("select * from web where id=?",list1)
result=c.fetchall()
if(result):
    print("welcome :",result[0])
    print("last updated value: ",result[0])
    print("what do you want?")
    print("enter 1 for deposit")
    print("enter 2 for withdrawn")
    x=int(input("enter your choice: "))
    if(x==1):
        z=input("enter the amount:")
        c.execute("select * from web where id=?",list1)
        result1=c.fetchall()
        a=result1[0][2]+z
        list2=[(a,x)]
        c.execute("update web set phn=123 where id=1")
        print("you have successfully deposited")
    if(x==2):
        y=input("enter the amount :")
        c.execute("select * from web where id=?",list1)
        result2=c.fetchall()
        b=result2[0][2]+y
        list3=[(b,x)]
        c.execute("update web set phn=123 where id=1")
        print("amount successfully withdrawn")
