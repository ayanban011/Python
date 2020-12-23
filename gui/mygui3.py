import sqlite3

mydb=sqlite3.connect('student.db')
c=mydb.cursor()
employee=[
            (1,'amit','kolkata'),
            (2,'raja','delhi'),
            (3,'rohan','kolkata'),
    ]
c.executemany('insert into stud_ values(?,?,?)',employee)
mydb.commit()
print("record inserted...")
