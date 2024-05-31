##main flask app :: Shahil kadia
###cd s:\programming\projects\doctor-appointment-system;Set-ExecutionPolicy Unrestricted -Scope Process;.\docvenv\Scripts\Activate.ps1
from flask import *
from flask import request, jsonify
from werkzeug.utils import secure_filename
from time import ctime
import logging
import logindbscript as db
import appointdbscript as apdb

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')
app.secret_key =  "DOCTOR_792739"
app.config['SECRET_KEY'] = "DOCTOR_792739"

@app.route('/')
def home():
    #return redirect(url_for('intro'))
    # logging.info("Main page accessed.")
    
    return render_template("test1.html")

@app.route('/home')
def select():
    return render_template('dash1.html')

@app.route('/doctorappointments/<docname>',methods=['GET', 'POST']) ##ready
def doctorappoint(docname):
    name=docname
    pending = apdb.reqpatientappoints(name)
    schedule = apdb.docfinal(name)
    try:
        for i in range(0,len(pending)):
            # print(f"value I = {i}")
            for j in range(0,len(schedule)):
                # print(f"value J = {j}")
                if(pending[i][0] == schedule[j][0]):
                    # print("remove trigger")
                    pending.remove(pending[i])
    except IndexError:
        pass
    output = pending
    if request.method == 'POST':
        name = request.form['patientName']
        id = request.form['patientID']
        date = request.form['appointmentDate']
        doctime = request.form['appointmentTime']
        confirm = request.form['confirmPatient']
        if confirm=='ACCEPT':
            print('accept')
            apdb.appointconf(pat=name,option=True,id=id,time=doctime)
        elif confirm=='REJECT':
            print('reject')
            apdb.appointconf(pat=name,option=False,id=id,time=doctime)
        # return f"Patient {id} request accepted."
        # return render_template('DocAppoint.html',output=output)
        # output = output[1:]
        # pending = apdb.reqpatientappoints(name)
        #  output = pending
        # schedule = apdb.docfinal(name)
        #  pending = apdb.reqpatientappoints(name)
        #  schedule = apdb.docfinal(name)
        # for i in pending:
        #     for j in schedule:
        #         if i[0]==j[0]:
        #             pending.remove(i)
        #             pass
        # try:
        #     for i in range(0,len(pending)):
        #         # print(f"value I = {i}")
        #         for j in range(0,len(schedule)):
        #             # print(f"value J = {j}")
        #             if(pending[i][0] == schedule[j][0]):
        #                 # print("remove trigger")
        #                 pending.remove(pending[i])
        # except IndexError:
        #     pass
        index=0
        pending = output
        print("len pending =",len(pending),len(output))
        print(pending)
        try:
            for i in range(0,len(pending)):
                if(pending[i][0]==int(id)):
                    index=i
        except:
            pass
        print(("index = "),index,("len pending = "),(len(pending))) 
        output.remove(pending[index])         
        return render_template('DocSchedulefinal.html',output=pending)
    return render_template('DocSchedulefinal.html',output=pending)

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
        return redirect(url_for('patientdashboard'))
    return render_template('patientForm.html',name=patname,output=output)


@app.route('/doctorlogin',methods=['GET', 'POST'])   #working
def doclogin():
    session.pop('pat_name',None)
    session.pop('doc_name',None)
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username,password)
        if db.load_doc(str(username),str(password)):
            name = db.getname_doc(username)
            session['doctor_name'] = name
            # return redirect(url_for('doctorappoint',docname=name))
            return redirect(url_for('doctordashboard'))
        else:
            print("flase")
            error = "Incorrect credentials ! "
            # return render_template('login.html')
    
        # return render_template('login.html')
    return render_template('idex-login-final.html',error=error)

@app.route('/doctorsignup',methods=['GET', 'POST'])
def docsignup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        # print(username,password)
        db.create_doc(username=username,password=password,name=name)
        return redirect(url_for('doclogin'))
    return render_template('docsignup.html',error=error)

@app.route('/patientlogin',methods=['GET', 'POST'])   #working
def patlogin():
    session.pop('pat_name',None)
    session.pop('doc_name',None)
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username,password)
        if db.load_user(str(username),str(password)):
            name = db.getname_user(username)
            session['pat_name'] = name
            # return redirect(url_for('doctorappoint',docname=name))
            return redirect(url_for('patientdashboard'))
        else:
            print("flase")
            error = "Incorrect credentials ! "
            # return render_template('login.html')
    
        # return render_template('login.html')
    return render_template('pat_signin.html',error=error)

@app.route('/patientsignup',methods=['GET', 'POST'])
def patsignup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        password = request.form['password']
        # print(username,password)
        db.create_user(username=username,password=password,name=name)
        return redirect(url_for('patlogin'))
    return render_template('signup_pat.html',error=error)




@app.route('/doctordashboard')
def doctordashboard():
    name = session['doctor_name']
    pending = apdb.reqpatientappoints(name)
    schedule = apdb.docfinal(name)
    # for i in pending:
    #     for j in schedule:
    #         if i[0]==j[0]:
    #             pending.remove(i)
    #             pass
    try:
        for i in range(0,len(pending)):
            # print(f"value I = {i}")
            for j in range(0,len(schedule)):
                # print(f"value J = {j}")
                if(pending[i][0] == schedule[j][0]):
                    # print("remove trigger")
                    pending.remove(pending[i])
    except IndexError:
        pass
    return render_template('Doctor_Dashboard.html',name=name,pending=pending,schedule=schedule)

@app.route('/patientdashboard')
def patientdashboard():
    name = session['pat_name']
    # pending = apdb.reqpatientappoints(name)
    # schedule = apdb.docfinal(name)
    all = apdb.patappoints(name)
    id =[]
    # status=dict{0:0,}
    status = []
    for i in all:
        id.append(i[0])
    for i in id:
        tstatus = apdb.patfinal(name,i)
        status.append(tstatus)
    return render_template('patient_dashboard.html',name=name,all=all,status=status,zip1=zip(all,status))

# @app.route('/patientdashboard')
# def patientdashboard():
#     return render_template('patient_dashboard.html')

#main runtime
if __name__ == '__main__':
    db.init_db()
    apdb.init_db()
    app.run(debug=False,port=8000)