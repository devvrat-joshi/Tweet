import sqlite3
connf = sqlite3.connect('followers.db')
cf = connf.cursor()
connu = sqlite3.connect('users.db')
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
        exist = cu.execute("""
        select username
        from users
        where username="{}"
        """.format(followed))#
        #in am calling you , pick upt the call
        for i in exist:
            exist = True
        else:
            exist = False
        if (not exist):
            return ""
        already = cf.execute("""
        select *
        from followers
        where follower="{}" and followed="{}"
        """.format(follower,followed))
        for i in already:
            already = True
        else:
            already = False
        if (already):
            return ""        
    except:
        pass

def remove_follower():
    