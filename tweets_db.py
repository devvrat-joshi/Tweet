# id, user, time, likes

import sqlite3
conn = sqlite3.connect('tweets.db')
c = conn.cursor()

# c.execute("DROP TABLE tweets;")
conn.commit()
c.execute("""
    CREATE TABLE IF NOT EXISTS tweets (
        tweet_id INTEGER PRIMARY KEY,
        username VARCHAR(80) NOT NULL,
        body VARCHAR(300) NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
""")

conn.commit()

def post_tweet(username,body):
    try:
        if not body:
            return "The body does not exists."
        c.execute("""
            INSERT INTO tweets (username, body)
            VALUES ('{}', '{}')
        """.format(username,body))
        conn.commit()
        return "Successfully posted"
    except:
        return "Tweet cannot be posted. Try again later."
# conn.commit()
