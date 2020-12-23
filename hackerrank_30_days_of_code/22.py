import sqlite3
db=sqlite3.connect("samp.db")
c=db.cursor()
c.execute("select * from web where id=7")
result=c.fetchall()
'''for i in result:
    print(i)'''
if(result):
    print("record found")
else:
    print("record not found")
