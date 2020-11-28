# id, user, time, likes
import sqlite3
conn = sqlite3.connect('minitweet.db')
c = conn.cursor()
conn2 = sqlite3.connect('minitweet.db')
c2 = conn2.cursor()

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

def does_user_exist(username):
    try:
        given_users = c.execute("""
            SELECT * FROM users
            WHERE username = "{}"
        """.format(username))
        for user in given_users:
            return True
        return False
    except:
        return False

def post_mention_update(from_user, target_user, tweet_id):
    body = from_user + " mentioned you in his tweet_id : " + str(tweet_id) + "."
    try:
        c.execute("""
            INSERT INTO updates (username, body)
            VALUES ('{}', '{}')
        """.format(target_user, body))
        conn.commit()
    except:
        pass

def get_mentions(username, body, tweet_id):
    body = body.split()
    mentions = []
    for word in body:
        if (word[0] == '@'):
            if does_user_exist(word[1:]):
                mentions.append(word[1: ])
    for mention in mentions:
        post_mention_update(username,mention,tweet_id)
    

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
        hashtags = get_hastags(body)
        for tag in hashtags:
            c.execute("INSERT INTO tags (tag, tweet_id) VALUES (?, ?)", (tag, tweet_id))
            conn.commit()
        get_mentions(username, body, tweet_id)
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
        res = ""
        rank = 1
        for trend in trends:
            res = res + ("#" + str(rank) + " " + trend[0] + " :: " + str(trend[1]) + "\n")
            rank += 1
        return res
    except:
        return "Cannot fetch trending hashtags."

def fetch_following(username):
    followingList = []
    try:
        followings = c2.execute("""
            SELECT followed from followers
            WHERE follower = ?
        """, (username,))
        for following in followings:
            followingList.append(following[0])
        return followingList
    except:
        return followingList

def parse_tweet(tweet_id, username, body, created_at):
    res = "{} : {} :: {} \n {} \n\n".format(username, created_at, tweet_id, body)
    return res

def fetch_feed(username, numTweets = 5, offsetPage = 1):
    tweets = []
    try:
        tweetsData = []
        following_list = fetch_following(username)
        if not following_list:
            return []
        query_text = "( '" + following_list[0] + "' "
        following_list = following_list[1:]
        for member in following_list:
            query_text += ", '" + member + "' "
        query_text += ")"
        dataRows = c.execute("""
            SELECT * from tweets
            WHERE username IN {a}
            ORDER BY created_at DESC
            LIMIT {c}
            OFFSET {b}
        """.format(a = query_text, c = numTweets, b= numTweets * (offsetPage - 1) ))
        for data in dataRows:
            tweets.append(parse_tweet(data[0], data[1], data[2], data[3]))
        return tweets
    except:
        return tweets