##main flask app :: Shahil kadia
###cd s:\programming\projects\doctor-appointment-system;Set-ExecutionPolicy Unrestricted -Scope Process;.\docvenv\Scripts\Activate.ps1
from flask import *
from flask import request, jsonify
from werkzeug.utils import secure_filename
import datetime
import os
import hashlib
import logindbscript as db
# import pytz
from time import ctime
import datetime
import time
import threading
from flask_cors import CORS
import logging

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

# CORS(app)
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

@app.route('/doctorappointments')
def doctorappoint():
    return render_template('DocSchedule.html')

@app.route('/doctorlogin',methods=['GET', 'POST'])
def doclogin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username,password)
        if db.load_user(str(username),str(password)):
            return redirect(url_for('doctorappoint'))
        else:
            print("flase")
            error = "Incorrect password !"
            # return render_template('login.html')
    
        # return render_template('login.html')
    return render_template('idex-login-final.html',error=error)
@app.route('/verifydoclogin',methods=['POST'])
def verifydoc():
    username = request.form['username']
    password = request.form['password']
    if db.load_user(username,password):
        return redirect(url_for('doctorappoint'))
    else:
        return render_template('idex-login-final.html')

#main runtime
if __name__ == '__main__':
    db.init_db()
    app.run(debug=True,port=8000)