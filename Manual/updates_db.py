import sqlite3
conn = sqlite3.connect('minitweet.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS updates (
        update_id INTEGER PRIMARY KEY,
        username VARCHAR(80) NOT NULL UNIQUE,
        body VARCHAR(300) NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        is_read BOOL DEFAULT 0
        );
""")

conn.commit()

def fetch_updates(username):
    try:
        updates = c.execute("""
                SELECT *
                FROM updates
                WHERE is_read = 0 AND username = '{}'
                ORDER BY created_at DESC
            """.format(username))
        body = ""
        up_num = 1
        for update in updates:
            body += "#" + str(up_num) + " :" + update[2] + "\n"
        if not body:
            return "No Updates.\n"
        return body
    except:
        return "Unable to fetch updates"

def mark_read(username):
    try:
        c.execute("""
            UPDATE updates
            SET is_read = 1
            WHERE username = '{}' AND is_read = 0
        """.format(username))
        conn.commit()
        return "All updates marked as read."
    except:
        return "Unable to mark as read"
