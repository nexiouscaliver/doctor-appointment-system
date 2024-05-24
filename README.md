
# Doctor Appointment System
## _Lightweight Appointment Service_

A Simple yet effective doctor appointment system that can run on remote server/local machine without any special requirements and host a webserver with easy and Intractive GUI for doctors and patients to book and check appointments.

## Features
- Lightweight & Easy to deploy
- Secured with additional hashing for passwords and sensitive information. 
- Uses a offline sql lite database server to run every child process in single server.
- Easy log generation for backtracing errors.

## Tech

- [Flask & WSGI] - Hosting Server
- [SQLite3] - Database server
- [HTML/CSS/JS] - Frontend
- [Python] - Backend 

And of course it is open source with a [public repository](https://github.com/nexiouscaliver/doctor-appointment-system/) on GitHub.


## Installation
It requires [Python](https://www.python.org/) v3.11+ to work perfectly.

Install the dependencies :
```sh
pip install -r requirements.txt
```

## Deployment

Start the server :
```sh
flask run app.py
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT ;)

**Free Software, Hell Yeah!**
