class bank:
    def __init__(self,x):
        self.x=x
        db=sqlite3.connect("bank2.db")
        c=db.cursor()
        script='''create table bank2(id integer primary key,name text,bal integer);
        insert into bank2(name,bal) values('cr7','1000');'''
class bank1(bank):
    def __init__(self,x):
        super().__init__(x)
    def getentry(self):
        q=int(input("enter id"))
        if(q==1):
            print("enter 1 for deposit")
            print("enter 2 for withdrawn")
            a=int(input("enter your choice"))
            return a
class bank3(bank1):
    def __init__(self,x):
        super().
        
                  
    
