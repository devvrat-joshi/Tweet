import sqlite3
connf = sqlite3.connect('minitweet.db')
cf = connf.cursor()
connu = sqlite3.connect('minitweet.db')
cu = connu.cursor()


cf.execute("""
    CREATE TABLE IF NOT EXISTS followers (
        follower VARCHAR(80) NOT NULL,
        followed VARCHAR(80) NOT NULL
        );
""")



connf.commit()

def add_follower(follower,followed):
    try:
        if (followed == follower):
            return "Cannot follow yourself"
        exist = cu.execute("""
            SELECT username
            FROM users
            WHERE username="{}"
        """.format(followed))#
        does_exist = False
        for i in exist:
            does_exist = True
        if does_exist == False:
            return "Invalid username"
        already = cf.execute("""
            SELECT *
            FROM followers
            WHERE follower="{}" and followed="{}"
        """.format(follower,followed))
        for i in already:
            return "Already following"
        cf.execute("""
            INSERT INTO followers VALUES ("{}","{}")
        """.format(follower,followed))
        cu.execute("""
            UPDATE users
            SET followers = followers + 1
            WHERE username = "{}";
        """.format(followed))
        connu.commit()
        cu.execute("""
            UPDATE users
            SET following = following + 1
            WHERE username = "{}";
        """.format(follower))
        connu.commit()
        return " successfully started following "+ followed
    except:
        return "Unable to follow"

def remove_follower(follower,followed):
    try:
        already = cf.execute("""
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
        cf.execute("""
            DELETE FROM followers
            WHERE follower="{}" and followed="{}"
        """.format(follower,followed))
        connf.commit()
        cu.execute("""
            UPDATE users
            SET followers = followers - 1
            WHERE username = "{}";
        """.format(followed))
        connu.commit()
        cu.execute("""
            UPDATE users
            SET following = following - 1
            WHERE username = "{}";
        """.format(follower))
        connu.commit()
        return "Successfully Unfollowed "+ followed
    except:
        return "Unable to unfollow"
