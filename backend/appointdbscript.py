import sqlite3 as sql


def init():
    con = sql.connect("appointment.db",check_same_thread=False)
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Appoint(AppID INT PRIMARY KEY AUTOINCREMENT,Pat_name varchar(100),Pat_dob DATE,Gender varchar(10),Pat_Contact int(11),Pat_Email varchar(100),Appoint_date DATE,Doc_Selected varchar(100),Pat_Symptoms varchar(100))")
    con.commit()
    con.close()
    return True

def appoint(name:str,dob:str,gen:str,cont:int,email:str,appoint_date:str,dr:str,sym:str):
    con = sql.connect("appointment.db",check_same_thread=False)
    cur=con.cursor()
    q= "INSERT INTO Appoint(Pat_name,Pat_dob,Gender,Pat_Contact,Pat_Email,Appoint_date,Doc_Selected,Pat_Symptoms) VALUES('{}','{}','{}',{},'{}','{}','{}','{}')".format(name,dob,gen,cont,email,appoint_date,dr,sym)
    cur=con.cursor()
    cur.execute(q)
    con.commit()
    con.close()
    return True
