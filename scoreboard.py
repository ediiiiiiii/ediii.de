import sqlite3 as sql
import sys
import os.path

path = sys.path[0] + "/scoreboard.db"

def check():
    if os.path.exists(path):
        return
    else:
        with sql.connect(path) as conn:
            db = conn.cursor()
            db.execute("CREATE TABLE scoreboard (username varchar(255), highscore int, PRIMARY KEY (username))")
            conn.commit()

def get_scores():
    with sql.connect(path) as conn:
        db = conn.cursor()
        db.execute("SELECT username, highscore FROM scoreboard ORDER BY highscore DESC")
        result = db.fetchall()
        print(result)
        return result

def set_score(username, score):
    scores = get_scores()
    
    for s in scores:
        if (s[0] == username):
            if (s[1] >= score):
                return
            with sql.connect(path) as conn: # update
                db = conn.cursor()
                db.execute(f"UPDATE scoreboard SET highscore = {score} WHERE username = \"{username}\"")
                return
    
    with sql.connect(path) as conn: # Insert new user
        db = conn.cursor()
        db.execute(f"INSERT INTO scoreboard (username, highscore) VALUES (\"{username}\", {score})")
        conn.commit()
check()
