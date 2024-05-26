# import sqlite3

# con=sqlite3.connect("appointment.db")

# cur=con.cursor()

# cur.execute("CREATE TABLE Appoint(AppID INT PRIMARY KEY AUTOINCREMENT,Pat_name varchar(100),Pat_dob,DATE,Gender varchar(10),Pat_Contact int(11),Pat_Email varchar(100),Appoint_date DATE,Doc_Selected varchar(100),Pat_Symptoms varchar(100))")

# cur.execute("INSERT INTO Appoint Values(1,'test','Dr.test','12am',2024-05=25)")
# cur.execute("UPDATE Appoint SET Date='2024-05-25' where ApNO = 1")
# con.commit()
#r=cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='Appoint'")
#print(r.fetchall())

from flask import Flask, render_template, redirect,request,url_for
import sqlite3 as sql
app = Flask(__name__)
con = sql.connect("appointment.db",check_same_thread=False)


@app.route('/',methods=["POST","GET"])
def appoint():
    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["dob"]
        gen = request.form["gender"]
        cont= request.form["contact"]
        email= str(request.form["email"])
        appoint_date= str(request.form["appointmentDate"])
        dr= request.form["doctor"]
        sym= request.form["symptoms"]
        #"CREATE TABLE Appoint(AppID INT PRIMARY KEY AUTOINCREMENT,Pat_name varchar(100),Pat_dob DATE,Gender varchar(10),Pat_Contact int(11),Pat_Email varchar(100),Appoint_date DATE,Doc_Selected varchar(100),Pat_Symptoms varchar(100))"
        # INSERT INTO Appoint(Pat_name,Pat_dob,Gender,Pat_Contact,Pat_Email,Appoint_date,Doc_Selected,Pat_Symptoms) VALUES('test','2025-02-06','male',9999999999,'test@gmail.com','2024-04-3','Dr.test1','Cough')
        q= "INSERT INTO Appoint(Pat_name,Pat_dob,Gender,Pat_Contact,Pat_Email,Appoint_date,Doc_Selected,Pat_Symptoms) VALUES('{}','{}','{}',{},'{}','{}','{}','{}')".format(name,dob,gen,cont,email,appoint_date,dr,sym)
        cur=con.cursor()
        cur.execute(q)
        con.commit()
        return "Appointment made Sucessfully"
    else:
        return render_template("index.html")




