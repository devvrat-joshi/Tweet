import sqlite3
conn = sqlite3.connect('minitweet.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(80) NOT NULL PRIMARY KEY UNIQUE,
        password VARCHAR(80) NOT NULL, 
        followers INT DEFAULT 0,
        following INT DEFAULT 0
        );
""")

conn.commit()

def register_check(username):
    try:
        given_users = c.execute("""
            SELECT * FROM users
            WHERE username = "{}"
        """.format(username))
        for user in given_users:
            return False
        return True
    except:
        return False
    
def register(username, password):
    if not register_check(username):
        return False
    try:
        c.execute("""
            INSERT INTO users (username, password)
            VALUES ('{}', '{}');
        """.format(username,password))
        conn.commit()
        return True
    except:
        return False

def login(username,password):
    try:
        given_users = c.execute("""
        SELECT * FROM users
        WHERE username = "{}" AND password = "{}"
        """.format(username,password))
        for user in given_users:
            return True
        return False
    except:
        return False
        
def view_profile(username):
    try:
        given_users = c.execute("""
            SELECT * FROM users
            WHERE username = "{}"
        """.format(username))
        does_exist = False
        curr_user = None
        for user in given_users:
            does_exist = True
            curr_user = user
        if not does_exist:
            return "Given username does not exists"
        return "{} :: Followers : {}, Following : {}".format(username,curr_user[2],curr_user[3]) 
    except:
        return "Invalid Username"

def search(pattern):
    try:
        given_users = c.execute("""
            SELECT username
            FROM users
            WHERE username LIKE "{}%"
            LIMIT 5
        """.format(pattern))
        res = ""
        for user in given_users:
            res += " # "+ user[0] + "\n"
        return "search results : \n" + res
    except Exception:
        print(Exception.with_traceback)
        return "Invalid search"