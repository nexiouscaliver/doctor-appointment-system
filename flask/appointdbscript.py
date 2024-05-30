import sqlite3
con=sqlite3.connect("appointment.db")
cur=con.cursor()

def init_db():
    con=sqlite3.connect("appointment.db")
    cur=con.cursor()
    q="CREATE TABLE IF NOT EXISTS appoint(Appno INTEGER PRIMARY KEY,Doc_Selected varchar(100),Time varchar(10))"
    cur.execute(q)
    q="CREATE TABLE IF NOT EXISTS appointconf(Appno INTEGER PRIMARY KEY,Time varchar(10),Pat varchar(100),Doctor varchar(100))"
    cur.execute(q)
    q="CREATE TABLE IF NOT EXISTS Appoint2(AppID INTEGER PRIMARY KEY AUTOINCREMENT,Pat_name varchar(100),Pat_dob DATE,Gender varchar(10),Pat_Contact int(11),Pat_Email varchar(100),Appoint_date DATE,Doc_Selected varchar(100),Pat_Symptoms varchar(500))"
    cur.execute(q)
    q="CREATE TABLE IF NOT EXISTS Reject(Appno INTEGER PRIMARY KEY,Pat_name varchar(100),Doc_name varchar(100))"
    cur.execute(q)
    con.commit()
    con.close()
    print("Appointdb init successfull")
    return True

def appoint(name:str,dob:str,gen:str,cont:int,email:str,appoint_date:str,dr:str,sym:str): #create pat appoint 
    # con = sql.connect("appointment.db",check_same_thread=False)
    # cur=con.cursor()
    con=sqlite3.connect("appointment.db")
    cur=con.cursor()
    q= "INSERT INTO Appoint2(Pat_name,Pat_dob,Gender,Pat_Contact,Pat_Email,Appoint_date,Doc_Selected,Pat_Symptoms) VALUES('{}','{}','{}',{},'{}','{}','{}','{}')".format(name,dob,gen,cont,email,appoint_date,dr,sym)
    cur=con.cursor()
    cur.execute(q)
    con.commit()
    con.close()
    return True

def appointconf(pat:str , option:bool , time:str=""):#func to confirm pat appoint.
        con=sqlite3.connect("appointment.db")
        cur=con.cursor()
        q="Select * from Appoint2 where Pat_name = '{}'".format(pat)
        e=cur.execute(q)
        x=e.fetchone()
        # op=input("Enter Y or N= ")
        if(option==True):
            # T=input("Enter time=")
            #CREATE Table appointconf(Appno INTEGER PRIMARY KEY,Time varchar(10),Doctor varchar(100))
            s = f"SELECT Doc_Selected FROM Appoint2 where Pat_name = '{pat}'"
            cur.execute(s)
            x1 = cur.fetchone()
            qu="INSERT INTO appointconf VALUES({},'{}','{}','{}')".format(x[0],time,pat,x1[0])
            cur.execute(qu)
            con.commit()
            print(f"Appointment {x[0]} is Confirmed")
            return True
        else:
            s = f"SELECT Doc_Selected FROM Appoint2 where Pat_name = '{pat}'"
            cur.execute(s)
            x1 = cur.fetchone()
            print(x)
            q = f"INSERT INTO Reject VALUES({x[0]},'{pat}','{x1[0]}')"
            cur.execute(q)
            con.commit()
            print(f"Appointment {x[0]} is Rejected")
            return True
        con.commit()
        con.close()
    
def reqpatientappoints(dr): #get list of all pat appointments
    con=sqlite3.connect("appointment.db")
    cur=con.cursor()
    q="Select * from Appoint2 where Doc_Selected = '{}'".format(dr)
    e=cur.execute(q)
    a=e.fetchall()
    # q="Select * from Reject where Doc_name = '{}'".format(dr)
    q = "Select * from Reject"
    e=cur.execute(q)
    b=e.fetchall()
    l=len(a)
    l2=len(b)
    # print(a,b)
    # print(l,l2)
    final=[]
    rejectlist=[]
    # if l2 == 0:l2=l2+1
    for i in range(0,l2):
        rejectlist.append(b[i][1])
    for i in range(0,l):
        if a[i][1] in rejectlist:
            continue
        else:
            print("Appointment of patient",a[i][0])
            print("Patient Name=",a[i][1])
            print("Appointment Date=",a[i][6])
            print("Patient Symptoms=",a[i][8])
            print()
            final.append([a[i][0],a[i][1],a[i][6],a[i][8]])

    con.commit()
    con.close()
    return final

def patappoints(pat):
    con=sqlite3.connect("appointment.db")
    cur=con.cursor()
    q="Select * from Appoint2 where Pat_name = '{}'".format(pat)
    e=cur.execute(q)
    a=e.fetchall()
    return a

def patfinal(pat_name,id): #recieve if pat appoint accept or reject
    con=sqlite3.connect("appointment.db")
    cur=con.cursor()
    q=""" Select appoint2.AppID,appoint2.Pat_name,appointconf.doctor,appointconf.time from appoint2,appointconf where appoint2.Doc_Selected = appointconf.Doctor AND appoint2.AppID = appointconf.Appno AND appoint2.Pat_name='{}' AND appoint2.AppID='{}' """.format(pat_name,id)
    e=cur.execute(q)
    a=e.fetchall()
    l=len(a)
    c=0
    for i in range(0,l):
        if (pat_name==a[i],[1]):
            c=1
            break
    
    if(c==1):
        print("Appoint Confirm")
        return "ACCEPT"
    else:
        q = f"SELECT Pat_name from Reject where Pat_name='{pat_name}'"
        e = cur.execute(q)
        o = e.fetchall()
        if len(o) == 0:
            print("Appoint pending")
            return "PENDING"
        else:
            print("Appoint Reject")
            return "REJECT"
        # print("Appoint Reject")
    con.commit()
    con.close()

def docfinal(Doc): #list all pat accept
    con=sqlite3.connect("appointment.db")
    cur=con.cursor()
    q=""" Select appoint2.AppID,appoint2.Pat_name,appointconf.doctor,appoint2.Appoint_date,appointconf.time,appoint2.Pat_Symptoms from appoint2,appointconf where appoint2.Doc_Selected = appointconf.Doctor AND appoint2.AppID = appointconf.Appno AND appointconf.Doctor='{}' """.format(Doc)
    e=cur.execute(q)
    a=e.fetchall()
    l=len(a)
    # print(a)
    c=0
    final = []
    if l==0:
        print("No Appointments")
    else:
        for i in range(0,l):
            if (Doc==a[i],[1]):
                c=1
                print(a[i],"Appoint Confirm")
                final.append(list(a[i]))
                break
    con.commit()
    con.close()
    return final
    
    # if(c==1):
    #     print("Appoint Confirm")
    # else:
    #     print("Appoint Reject")
