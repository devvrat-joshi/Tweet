"""
Contains basic functions for command related to followers:

- add_follower(follower,followed): to add 'follower' as a follower to user 'followed'
- remove_follower(follower,followed): to remove follower 'follower' as a follower to user 'followed'
- fetch_online(username): to fetch the list of followers (both online and offline) for the given username (this is used as a utility function to check which followers are online)
- is_follower(username, target_user): return True or False if 'username' is follower of 'target_user'
"""


import sqlite3
from colorama import init, Fore, Back, Style
conn = sqlite3.connect('minitweet.db')
c = conn.cursor()

#create the followers table
c.execute("""
    CREATE TABLE IF NOT EXISTS followers (
        follower VARCHAR(80) NOT NULL,
        followed VARCHAR(80) NOT NULL
        );
""")

conn.commit()

def add_follower(follower,followed):
    try:
        #cannot follower itself case
        if (followed == follower):
            return Fore.RED + "Cannot follow yourself" + Fore.WHITE
        #check if the followed username exists
        exist = c.execute("""
            SELECT username
            FROM users
            WHERE username="{}"
        """.format(followed))#
        does_exist = False
        for i in exist:
            does_exist = True
        if does_exist == False:
            return Fore.RED + "Invalid username" + Fore.WHITE
        #check if already following
        already = c.execute("""
            SELECT *
            FROM followers
            WHERE follower="{}" and followed="{}"
        """.format(follower,followed))
        for i in already:
            return Fore.BLUE + "Already following" + Fore.WHITE
        #set as follower and increment followers for 'followed' and increment following numbers for 'follower'
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
        return Fore.GREEN + " successfully started following " + Fore.BLUE + followed + Fore.WHITE
    except:
        return Fore.RED + "Unable to follow" + Fore.WHITE

def remove_follower(follower,followed):
    try:
        #in case not a follower
        already = c.execute("""
            SELECT *
            FROM followers
            WHERE follower="{}" and followed="{}"
        """.format(follower,followed))
        does_follow = False
        for i in already:
            does_follow = True
        if does_follow != True:
            return Fore.RED + "Unable to unfollow" + Fore.WHITE
        #delete from table
        c.execute("""
            DELETE FROM followers
            WHERE follower="{}" and followed="{}"
        """.format(follower,followed))
        conn.commit()
        #decrement the followers and following  data for respective users
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
        return Fore.GREEN + "Successfully Unfollowed "+ Fore.BLUE + followed + Fore.WHITE
    except:
        return Fore.RED + "Unable to unfollow" + Fore.WHITE

def fetch_online(username):
    followers_list = []
    try:
        #fetch the list of followers for username
        dataRows = c.execute("""
            SELECT follower
            FROM followers 
            where followed = '{u}'
        """.format(u = username))
        for data in dataRows:
            followers_list.append(data[0])
        return followers_list
    except:
        return followers_list

def is_follower(username, target_user):
    try:
        dataRows = c.execute("""
            SELECT follower
            FROM followers 
            where followed = '{u}' AND follower='{t}'
        """.format(u = username,t=target_user))
        for data in dataRows:
            return True
        return False
    except:
        return False