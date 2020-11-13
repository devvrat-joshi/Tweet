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



# conn.commit()

# all_users = c.execute("""
#     SELECT *
#     FROM users
# """)
# for i in all_users:
#     print(i)

# single user query with username and password
# given_user = c.execute("""
#     SELECT * FROM users
#     WHERE username = "{}"
# """.format("sachin"))

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