##main flask app :: Shahil kadia
###cd s:\programming\projects\doctor-appointment-system;Set-ExecutionPolicy Unrestricted -Scope Process;.\docvenv\Scripts\Activate.ps1
from flask import *
from flask import request, jsonify
from werkzeug.utils import secure_filename
import datetime
import os
import hashlib
from time import ctime
import datetime
import time
import threading
from flask_cors import CORS
import logging
import logindbscript as db
import appointdbscript as apdb

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')
app.secret_key =  "DOCTOR_792739"
#app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=360000)
#app.config['SESSION_PERMANENT']=True
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLDER = os.path.join(APP_ROOT, 'down_files')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# TEMP_FOLDER = os.path.join(APP_ROOT, 'temp_files')
# app.config['TEMP_FOLDER'] = TEMP_FOLDER
app.config['SECRET_KEY'] = "DOCTOR_792739"
@app.route('/')
def home():
    #return redirect(url_for('intro'))
    logging.info("Main page accessed.")
    
    return("<p1> HELLO WORLD")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/doctorappointments/<docname>',methods=['GET', 'POST']) ##ready
def doctorappoint(docname):
    output = apdb.reqpatientappoints(docname)
    if request.method == 'POST':
        name = request.form['patientName']
        id = request.form['patientID']
        date = request.form['appointmentDate']
        doctime = request.form['appointmentTime']
        confirm = request.form['confirmPatient']
        if confirm=='ACCEPT':
            print('accept')
            apdb.appointconf(pat=name,option=True,time=doctime)
        elif confirm=='REJECT':
            print('reject')
            apdb.appointconf(pat=name,option=False,time=doctime)
        # return f"Patient {id} request accepted."
        # return render_template('DocAppoint.html',output=output)
        output = output[1:]
        return render_template('DocSchedulefinal.html',output=output)
    return render_template('DocSchedulefinal.html',output=output)

@app.route('/scheduleappointment/<patname>',methods=['GET', 'POST'])
def scheduleappoint(patname):
    output = db.getalldoc()
    if request.method == 'POST':
        name = request.form['fullName']
        dob = request.form['dob']
        gender = request.form['gender']
        contact = request.form['contact']
        email = request.form['email']
        # address = request.form['address']
        docname = request.form['doctor']
        date = request.form['appointmentDate']
        symptoms = request.form['symptoms']
        print(name,dob,gender,contact,email,docname,date,symptoms)
        apdb.appoint(name=name,dob=dob,gen=gender,cont=contact,email=email,appoint_date=date,dr=docname,sym=symptoms)

        pass
    return render_template('patientForm.html',name=patname,output=output)


@app.route('/doctorlogin',methods=['GET', 'POST'])   #working
def doclogin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username,password)
        if db.load_user(str(username),str(password)):
            name = db.getname_doc(username)
            session['doctor_name'] = name
            return redirect(url_for('doctorappoint',docname=name))
        else:
            print("flase")
            error = "Incorrect credentials ! "
            # return render_template('login.html')
    
        # return render_template('login.html')
    return render_template('idex-login-final.html',error=error)


#main runtime
if __name__ == '__main__':
    db.init_db()
    apdb.init_db()
    app.run(debug=True,port=8000)