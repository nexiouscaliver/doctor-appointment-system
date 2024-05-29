import sqlite3
import hashlib
import logging
import sys
import os

print("DB CWD : ",os.getcwd())
###global variables
dbname = "data.db"      #enter your db name

###logging
logging.basicConfig(level=logging.INFO,filename='db.log',format='%(asctime)s - %(process)d - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Server Restarted :: App Started')     #sql logging start

###SQL server initialization
def init_db():
    print("SQL init started.")
    logging.warning("SQL init started.")
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    q1 = "CREATE TABLE IF NOT EXISTS user(id int auto increment , username text primary key, password text, name text);"
    cur.execute(q1)
    cur.close()
    conn.commit()
    conn.close()
    print("SQL init compleated!")
    logging.warning("SQL init compleated!")

###sql definations
def create_user(username:str,password:str,name:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    logging.info(f"Connected to DB :: Creating user {username}")
    hpass = hashlib.md5(password.encode()).hexdigest()
    sql = f'insert into user(username,password,name) values ("{username}","{hpass}","{name}");'
    try:
        cur.execute(sql)
        print(f"User {username}::{password} successfully generated")
        logging.info(f"User {username} successfully generated")
        return True
    except sqlite3.Error as error:
        print(f"SQL Error Occured:: {username} :: {error}")
        logging.error(f"SQL Error Occured:: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        logging.error(f"PY Error Occured:: {username} :: {e}", exc_info=True)
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()
        logging.info(f"Connection to DB closed :: User {username} created")

def load_user(username:str,password:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    logging.info(f"Connected to DB :: Loading user {username}")
    uhpass = hashlib.md5(password.encode()).hexdigest()
    sql = f'select password from user where username="{username}";'
    try:
        cur.execute(sql)
        shpass = cur.fetchall()
        print(shpass)
        if shpass == []:
            print(f"USER User {username} not found")
            logging.error(f"USER User {username} not found")
            return False
        elif uhpass == shpass[0][0]:
            print(f"User {username} has correct password {password}")
            logging.info(f"User {username} has correct password")
            return True
        elif shpass == []:
            print(f"USER User {username} not found")
            logging.error(f"USER User {username} not found")
            return False
        else:
            print(f"USER Incorrect password :: {username}")
            # logging.log(logging.INFO,f"USER Incorrect password :: {username}")
            logging.error(f"USER Incorrect password :: {username}")
            return False
    except sqlite3.Error as error:
        print(f"SQL Error occured :: {username} :: {error}")
        logging.error(f"SQL Error occured :: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        logging.error(f"PY Error Occured:: {username} :: {e}", exc_info=True)
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()
        logging.info(f"Connection to DB closed :: User {username} loaded")

def getname(username:str):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    logging.info(f"Connected to DB :: fetching name {username}")
    sql = f'select name from user where username="{username}";'
    try:
        cur.execute(sql)
        shpass = cur.fetchall()
        print(shpass)
        if shpass == []:
            print(f"USER User {username} not found")
            logging.error(f"USER User {username} not found")
            return False
        if shpass:
            print(f"User {username} has correct name {shpass[0][0]}")
            logging.info(f"User {username} has correct name")
            return shpass[0][0]
        else:
            print(f"USER Incorrect password :: {username}")
            # logging.log(logging.INFO,f"USER Incorrect password :: {username}")
            logging.error(f"USER Incorrect password :: {username}")
            return False
    except sqlite3.Error as error:
        print(f"SQL Error occured :: {username} :: {error}")
        logging.error(f"SQL Error occured :: {username} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {username} :: {e}")
        logging.error(f"PY Error Occured:: {username} :: {e}", exc_info=True)
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()
        logging.info(f"Connection to DB closed :: User {username} loaded")

def runquery(q):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        cur.execute(q)
        print(f"successfully run")
        logging.info(f"successfully run")
        return True
    except sqlite3.Error as error:
        print(f"SQL Error Occured:: {q} :: {error}")
        logging.error(f"SQL Error Occured:: {q} :: {error}")
        return False
    except Exception as e:
        print(f"PY Error Occured:: {q} :: {e}")
        logging.error(f"PY Error Occured:: {q} :: {e}", exc_info=True)
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()
        logging.info(f"Connection to DB closed :: successfully run")

#init once
# init_db()