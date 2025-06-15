import random
import string
import mysql.connector

storage = {}
    
def passwd_gen() -> str:
    total = string.ascii_letters + string.digits + string.punctuation
    count = 18
    result = ''.join(random.sample(total, count))
    return result

def adduser(username: str)  -> None:
    storage[username] = passwd_gen()
    
def remuser(username: str) -> None:
    storage.pop(username)

def add_entry(link_res: str, login: str) -> None:
    password = passwd_gen()
    dbconfig = {'host':'127.0.0.1',
                'user':'PassMan',
                'password':'qwe123',
                'database':'passmandb'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into storage
              (link, login, password)
              values
              (%s, %s, %s)"""
    cursor.execute(_SQL, (link_res, login, password))
    conn.commit()
    cursor.close()
    conn.close()
