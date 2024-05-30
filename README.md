
# Doctor Appointment System

This project aims to streamline the process of booking appointments with healthcare providers. Whether you're a patient looking to schedule a consultation or a healthcare professional managing appointments, this system provides a user-friendly interface to facilitate the appointment booking process efficiently.

## _Lightweight Appointment Service_

A Simple yet effective doctor appointment system that can run on remote server/local machine without any special requirements and host a webserver with easy and Intractive GUI for doctors and patients.

## Features
- Lightweight & Easy to deploy
- Secured with additional hashing for passwords and sensitive information. 
- Uses a offline sql lite database server to run every child process in single server.
- Easy log generation for backtracing errors.

## Tech

- [Flask & WSGI] - Hosting Server
- [Jinja2] - Render Frontend
- [SQLite3] - Lite Database server
- [HTML/CSS/JS] - Frontend
- [Python] - Backend 

And of course it is open source with a [public repository](https://github.com/nexiouscaliver/doctor-appointment-system/) on GitHub.

## System Requirments :

- Min. 1GB RAM
- Min. 2GB Free space
- Win/Linux/Unix Operating System (tested on Windows11/Linux/Rpi4)
- Python(v3.11+)

## Download

Clone the repository from github :
```sh
git clone https://github.com/nexiouscaliver/doctor-appointment-system.git
```

## Installation
It requires [Python](https://www.python.org/) v3.11+ to work perfectly.

Change directory:
```sh
cd doctor-appointment-system/
```

Install the dependencies :
```sh
pip install -r requirements.txt
```


## Deployment

Change to directory flask:
```sh
cd doctor-appointment-system/flask
```

Start the server :
```sh
flask run app.py
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
http://127.0.0.1:8000
```

## License

MIT ;)

**Free Software, Hell Yeah!**
