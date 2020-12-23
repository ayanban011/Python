import sqlite3

mydb=sqlite3.connect('student.db')
c=mydb.cursor()
c.execute('create table stud_(id integer,name text,addr text)')
mydb.commit()
print("database and table created...")
