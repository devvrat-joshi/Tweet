# id, user, time, likes

import sqlite3
conn = sqlite3.connect('minitweet.db')
c = conn.cursor()

# c.execute("DROP TABLE tweets;")
conn.commit()
c.execute("""
    CREATE TABLE IF NOT EXISTS tweets (
        tweet_id INTEGER PRIMARY KEY,
        username VARCHAR(80) NOT NULL,
        body VARCHAR(300) NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (username) REFERENCES users(username)
        );
""")

conn.commit()

c.execute("""
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY,
        tag VARCHAR(80) NOT NULL,
        tweet_id INTEGER NOT NULL,
        FOREIGN KEY (tweet_id) REFERENCES tweets(tweet_id)
    );
""")

conn.commit()

def get_hastags(body):
    body = body.split()
    tags = []
    for word in body:
        if (word[0] == '#'):
            tags.append(word[1: ])
    return tags

def post_tweet(username,body):
    try:
        if not body:
            return "The body does not exists."
        c.execute("""
            INSERT INTO tweets (username, body)
            VALUES ('{}', '{}')
        """.format(username,body))
        conn.commit()
        post_id_cursor = c.execute("""
            SELECT last_insert_rowid();
        """)
        tweet_id = post_id_cursor.fetchone()[0]
        print(tweet_id)
        hashtags = get_hastags(body)
        for tag in hashtags:
            c.execute("INSERT INTO tags (tag, tweet_id) VALUES (?, ?)", (tag, tweet_id))
            conn.commit()
        return "Successfully posted"
    except:
        return "Tweet cannot be posted. Try again later."

def fetch_trending():
    try:
        trends = c.execute("""
            SELECT tags.tag, COUNT(*)
            FROM tags
            INNER JOIN tweets ON tags.tweet_id=tweets.tweet_id
            WHERE tweets.created_at >= datetime('now','-1 day')
            GROUP BY tags.tag
            ORDER BY 2 DESC
            LIMIT 5;
        """)
        print(trends)
        res = ""
        rank = 1
        for trend in trends:
            print(trend)
            res = res + ("#" + str(rank) + " " + trend[0] + " :: " + str(trend[1]) + "\n")
            rank += 1
        return res
    except:
        return "Cannot fetch trending hashtags."