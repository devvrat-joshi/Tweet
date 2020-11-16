import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(80) NOT NULL PRIMARY KEY UNIQUE,
        password VARCHAR(80) NOT NULL 
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
            INSERT INTO users VALUES ('{}', '{}');
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


# conn.close()