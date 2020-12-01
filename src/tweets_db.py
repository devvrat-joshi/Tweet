# id, user, time, likes
import sqlite3
from colorama import init, Fore, Back, Style
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

c.execute("""
    CREATE TABLE IF NOT EXISTS pins (
        id INTEGER PRIMARY KEY,
        username VARCHAR(80) NOT NULL,
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

def post_retweet_update(from_user, target_user, tweet_id):
    try:
        body = from_user + " retweeted your tweet" + str(tweet_id) + ". "
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
        return Fore.GREEN + "Successfully posted" + Fore.WHITE 
    except:
        return Fore.RED + "Tweet cannot be posted. Try again later." + Fore.WHITE

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
            res = res + (Fore.BLUE + "#" + str(rank) + Fore.WHITE + " " + trend[0] + " :: " + str(trend[1]) + "\n")
            rank += 1
        return res
    except:
        return Fore.RED + "Cannot fetch trending hashtags." + Fore.WHITE

def fetch_following(username):
    followingList = []
    try:
        followings = c.execute("""
            SELECT followed from followers
            WHERE follower = ?
        """, (username,))
        for following in followings:
            followingList.append(following[0])
        return followingList
    except:
        return followingList

def parse_tweet_body(body):
    res = body.split()
    lenb = len(res)
    for i in range(lenb):
        if res[i][0] in ['#', '@']:
            res[i] = Fore.CYAN + res[i] + Fore.WHITE
    return " ".join(res)

def parse_tweet(tweet_id, username, body, created_at):
    res =  Fore.MAGENTA + username + Fore.WHITE + " : " + Fore.CYAN + created_at + Fore.WHITE + " :: " + Fore.BLUE + str(tweet_id) + Fore.WHITE+ "\n" + parse_tweet_body(body) + "\n\n"
    return res

def fetch_feed(username, numTweets = 5, offsetPage = 1):
    tweets = []
    try:
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

def fetch_tweets_by_tag(hashtag, numTweets = 5, numPage = 1):
    tweets = []
    try:
        dataRows = c.execute("""
            SELECT * from tweets
            INNER JOIN tags ON tags.tweet_id=tweets.tweet_id
            WHERE tags.tag = '{t}'
            LIMIT {l}
            OFFSET {o}
        """.format(t = hashtag, l = numTweets, o = numTweets * (numPage - 1)))
        for data in dataRows:
            tweets.append(parse_tweet(data[0], data[1], data[2], data[3]))
        return tweets
    except:
        return tweets

def fetch_posts(username, numTweets = 5, numPage = 1):
    tweets = []
    try:
        dataRows = c.execute("""
            SELECT * from tweets
            WHERE username = '{u}'
            ORDER BY created_at DESC
            LIMIT {l}
            OFFSET {o}
        """.format(u = username, l = numTweets, o = numTweets * (numPage - 1)))
        for data in dataRows:
            tweets.append(parse_tweet(data[0], data[1], data[2], data[3]))
        return tweets
    except:
        return tweets

def pin_tweet(username, tweet_id):
    try:
        pinned_rows = c.execute("""
        SELECT * from pins 
        WHERE username = '{u}' AND tweet_id = {t}
        """.format(u = username,t = tweet_id))
        for row in pinned_rows:
            return False
        c.execute("""
        INSERT INTO pins (username, tweet_id)
        VALUES ('{u}', {t})
        """.format(u = username,t = tweet_id))
        conn.commit()
        return True
    except:
        return False

def retweet_id(username, tweet_id):
    try:
        found_tweets = c.execute("""
            SELECT * from tweets
            WHERE tweet_id = {t}
        """.format(t = tweet_id))
        tweet_body = ""
        for tweet in found_tweets:
            target_user = tweet[1]
            tweet_body = "** Retweeted ** username: {u} tweet_id : {t}\n".format(u = target_user, t = tweet_id)
            tweet_body += tweet[2]
            post_tweet(username, tweet_body)
            post_retweet_update(username, target_user, tweet_id)
            return Fore.GREEN + "Retweet Successful" + Fore.WHITE
        return Fore.RED + "Cannot Retweet" + Fore.WHITE
    except:
        return Fore.RED + "Cannot Retweet" + Fore.WHITE