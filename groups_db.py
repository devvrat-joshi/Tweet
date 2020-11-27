import sqlite3
conn = sqlite3.connect('minitweet.db')
c = conn.cursor()
conn2 = sqlite3.connect('minitweet.db')
c2 = conn2.cursor()


c.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        groupname VARCHAR(80) NOT NULL PRIMARY KEY UNIQUE,
        username VARCHAR(80) NOT NULL,
        members INT DEFAULT 0
        );
""")

conn.commit()

c.execute("""
    CREATE TABLE IF NOT EXISTS groupmembers (
        group_id INTEGER PRIMARY KEY,
        groupname VARCHAR(80) NOT NULL,
        username VARCHAR(80) NOT NULL
        );
""")

conn.commit()

def does_user_exists(username):
    try:
        given_users = c2.execute("""
            SELECT * FROM users
            WHERE username = "{}"
        """.format(username))
        for user in given_users:
            return True
        return False
    except:
        return False

def does_group_exists(groupname):
    try:
        given_groups = c2.execute("""
            SELECT * FROM groups
            WHERE groupname = "{}"
        """.format(groupname))
        for group in given_groups:
            return True
        return False
    except:
        return True

def is_group_owner(username, groupname):
    try:
        given_rows = c2.execute("""
            SELECT * FROM groups
            WHERE groupname = "{}" AND username = "{}"
        """.format(groupname, username))
        for row in given_rows:
            return True
        return False
    except:
        return False

def does_member_exists(username, groupname):
    try:
        given_rows = c.execute("""
            SELECT * FROM groupmembers
            WHERE groupname = "{}" AND username = "{}"
        """.format(groupname, username))
        for i in given_rows:
            return True
        return False
    except:
        return False

def create_group(username, groupname):
    try:
        if does_group_exists(groupname):
            return "Groupname already taken!"
        c.execute("""
            INSERT INTO groups (groupname, username)
            VALUES ('{}', '{}')
        """.format(groupname, username))
        conn.commit()
        usernames = [username] #Group Owner Added
        add_member(username, usernames, groupname)
        return "Group Created"
    except:
        return "Unable to create the group"


def add_member(username, add_names, groupname):
    if not is_group_owner(username,groupname):
        return "You are not the owner of the group, contact group admin"
    added = []
    try:
        for user in add_names:
            if does_user_exists(user) and not does_member_exists(user, groupname):
                c.execute("""
                    INSERT INTO groupmembers (groupname, username)
                    VALUES ('{}', '{}')
                """.format(groupname, user))
                conn.commit()
                c.execute("""
                    UPDATE groups
                    SET members = members + 1
                    WHERE groupname = "{}";
                """.format(groupname))
                conn.commit()
                added.append(user)
    except:
        pass
    finally:
        return " ".join(added) + " added in " + groupname

def remove_member(username, remove_names, groupname):
    if not is_group_owner(username,groupname):
        return "You are not the owner of the group, contact group admin"
    deleted = []
    try:
        for user in remove_names:
            if does_member_exists(user, groupname):
                c.execute("""
                    DELETE FROM groupmembers
                    WHERE groupname ='{}' AND username = '{}'
                """.format(groupname, user))
                conn.commit()
                c.execute("""
                    UPDATE groups
                    SET members = members - 1
                    WHERE groupname = "{}";
                """.format(groupname))
                conn.commit()
                deleted.append(user)
    except:
        pass
    finally:
        return " ".join(deleted) + " deleted in " + groupname + "\n"

def fetch_members(username,groupname, for_chat = False):
    try:
        if does_member_exists(username, groupname):
            fetch_mems = c.execute("""
                SELECT *
                FROM groupmembers
                WHERE groupname = '{}'
            """.format(groupname))
            conn.commit()
            members = []
            for member in fetch_mems:
                if not for_chat and is_group_owner(member[2], groupname):
                    members.append(member[2] + "(OWNER)")
                else:
                    members.append(member[2])
            return members
        return []
    except:
        return []

def remove_group(username, groupname):
    try:
        if is_group_owner(username, groupname):
            c.execute("""
                DELETE FROM groups
                WHERE groupname ='{}'
            """.format(groupname))
            conn.commit()
            c.execute("""
                DELETE FROM groupmembers
                WHERE groupname ='{}'
            """.format(groupname))
            conn.commit()
            return "Group " + groupname + " deleted successfully!!!"
        else:
            return "You are not the owner of the group, contact group admin"
    except:
        return "Unable to delete the group"