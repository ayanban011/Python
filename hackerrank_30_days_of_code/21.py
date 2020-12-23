import sqlite3
db=sqlite3.connect("samp.db")
c=db.cursor()
c.execute("select * from web")
result=c.fetchall()
for i in result:
    print(i)
