import sqlite3
conn = sqlite3.connect('minitweet.db')
c = conn.cursor()


c.execute("""
    CREATE TABLE IF NOT EXISTS followers (
        follower VARCHAR(80) NOT NULL,
        followed VARCHAR(80) NOT NULL
        );
""")

conn.commit()

def add_follower(follower,followed):
    try:
        if (followed == follower):
            return "Cannot follow yourself"
        exist = c.execute("""
            SELECT username
            FROM users
            WHERE username="{}"
        """.format(followed))#
        does_exist = False
        for i in exist:
            does_exist = True
        if does_exist == False:
            return "Invalid username"
        already = c.execute("""
            SELECT *
            FROM followers
            WHERE follower="{}" and followed="{}"
        """.format(follower,followed))
        for i in already:
            return "Already following"
        c.execute("""
            INSERT INTO followers VALUES ("{}","{}")
        """.format(follower,followed))
        c.execute("""
            UPDATE users
            SET followers = followers + 1
            WHERE username = "{}";
        """.format(followed))
        conn.commit()
        c.execute("""
            UPDATE users
            SET following = following + 1
            WHERE username = "{}";
        """.format(follower))
        conn.commit()
        return " successfully started following "+ followed
    except:
        return "Unable to follow"

def remove_follower(follower,followed):
    try:
        already = c.execute("""
            SELECT *
            FROM followers
            WHERE follower="{}" and followed="{}"
        """.format(follower,followed))
        does_follow = False
        for i in already:
            does_follow = True
        if does_follow != True:
            return "Unable to unfollow"
        # DELETE ROW
        c.execute("""
            DELETE FROM followers
            WHERE follower="{}" and followed="{}"
        """.format(follower,followed))
        conn.commit()
        c.execute("""
            UPDATE users
            SET followers = followers - 1
            WHERE username = "{}";
        """.format(followed))
        conn.commit()
        c.execute("""
            UPDATE users
            SET following = following - 1
            WHERE username = "{}";
        """.format(follower))
        conn.commit()
        return "Successfully Unfollowed "+ followed
    except:
        return "Unable to unfollow"

def fetch_online(username):
    pass
