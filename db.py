import sqlite3 as sql
import sys

path = sys.path[0] + "/orakel.db"


def add_request(id, name, desc):
    with sql.connect(path) as conn:
        db = conn.cursor()
        db.execute(f"INSERT INTO requests (id, name, desc) VALUES ({id}, '{name}', '{desc}')")
        conn.commit()

def get_request(id):
    with sql.connect(path) as conn:
        db = conn.cursor()
        db.execute(f"SELECT name, desc FROM requests WHERE id = {id}")
        result = db.fetchall()
        if len(result) == 1:
            return result[0][0], result[0][1]
        else:
            return None, None

def get_user_name(name):
    with sql.connect(path) as conn:
        db = conn.cursor()
        db.execute(f"SELECT desc FROM users WHERE LOWER(name) = '{name.lower()}'")
        result = db.fetchall()
        if (len(result) >= 1):
            return result[0][0]
        else:
            return None

def add_user(id, name, desc):
    with sql.connect(path) as conn:
        db = conn.cursor()
        db.execute(f"DELETE FROM requests WHERE id = {id}")
        db.execute(f"INSERT INTO users (id, name, desc) VALUES ({id}, '{name}', '{desc}')")
        conn.commit()

def reset_db():
    print(path)
    with sql.connect(path) as conn:
        db = conn.cursor()
        try:
            db.execute("DROP TABLE requests")
            db.execute("DROP TABLE users")
        except sql.OperationalError:
            pass

        db.execute("CREATE TABLE requests (id INTEGER PRIMARY KEY, name VARCHAR(20), desc VARCHAR(200))")
        db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name VARCHAR(20), desc VARCHAR(200))")

        conn.commit()


#reset_db()
#add_request("934985887043", "Jonas", "mag Autos")
#print(get_user_name("Dieter"))
#add_user("934985887043")
