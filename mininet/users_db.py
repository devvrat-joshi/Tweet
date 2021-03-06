import sqlite3
from colorama import init, Fore, Back, Style
conn = sqlite3.connect('minitweet.db')
c = conn.cursor()
conn2 = sqlite3.connect('minitweet.db')
c2 = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(80) NOT NULL PRIMARY KEY UNIQUE,
        password VARCHAR(80) NOT NULL, 
        followers INT DEFAULT 0,
        following INT DEFAULT 0,
        is_online BOOL DEFAULT 1
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
            c.execute("""
                UPDATE users
                SET is_online = 1
                WHERE username = '{}'
            """.format(username))
            conn.commit()
            return True
        return False
    except:
        return False

def logout(username):
    try:
        c.execute("""
                UPDATE users
                SET is_online = 0
                WHERE username = '{}'
            """.format(username))
        conn.commit()
        return True
    except:
        return False

def parse_tweet_body(body):
    res = body.split()
    lenb = len(res)
    for i in range(lenb):
        if res[i][0] in ['#', '@']:
            res[i] = Fore.CYAN + res[i] + Fore.WHITE
    return " ".join(res)

def parse_tweet(tweet_id, body, created_at):
    res = "{} :: {} \n {} \n\n".format(created_at, tweet_id, body)
    return res

def fetch_pinned_tweets(username):
    tweets = []
    try:
        pinned_tweets = c.execute(
            """
                SELECT tweets.tweet_id, pins.username, tweets.body, tweets.created_at
                FROM pins
                INNER JOIN tweets on pins.tweet_id=tweets.tweet_id
                WHERE pins.username = "{u}"
                ORDER BY id DESC
                LIMIT 5
            """.format(u=username))
        for data in pinned_tweets:
            print(data)
            tweets.append(parse_tweet(data[0], data[2], data[3]))
        print(tweets)
        return tweets
    except:
        return tweets
        
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
        res = "{} :: Followers : {}, Following : {}\n".format(username,curr_user[2],curr_user[3]) 
        pinned_tweets = fetch_pinned_tweets(username)
        for tweets in pinned_tweets:
            res += tweets
        return res
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
