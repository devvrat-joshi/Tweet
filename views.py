import users_db,followers_db,tweets_db, updates_db, groups_db
import socket
tokenCounter = 1
logData = {}
toSessionID = {}

def init(data):
    global tokenCounter
    tokenCounter += 1
    return str(tokenCounter)

def login(data):
    if len(data) != 3:
        return "Invalid arguments"
    username, password,sessionID = data
    if sessionID in logData:
        return "Already logged in!"
    if users_db.login(username,password):
        logData[sessionID] = username
        toSessionID[username] = sessionID
        return "Logged in Successfully!"
    return "Invalid Username/Password"

def register(data):
    if len(data) != 4:
        return "Invalid arguments"
    username, password, repassword, sessionID = data
    if sessionID in logData:
        return "Already logged in!"
    elif password != repassword:
        return "Password doesn't match"
    elif users_db.register(username, password):
        logData[sessionID] = username
        toSessionID[username] = sessionID
        return "Welcome to the mini-tweet team, " + username + " !!!"
    else:
        return "User already exists"

def logout(data):
    if len(data) != 1:
        return "Invalid arguments"
    sessionID = data[0]
    if sessionID not in logData:
        return "Need to be logged in first."
    else:
        if users_db.logout(logData[sessionID]):
            toSessionID.pop(logData[sessionID])
            logData.pop(sessionID)
            return "$Logged_out$"
        else:
            return "Cannot logout"

def add_follower(data):
    if len(data) != 2:
        return "Invalid arguments"
    followed, sessionID = data
    if sessionID not in logData:
        return "Need to login first"
    follower = logData[sessionID]
    return followers_db.add_follower(follower, followed)

def remove_follower(data):
    if len(data) != 2:
        return "Invalid arguments"
    followed, sessionID = data
    if sessionID not in logData:
        return "Need to login first"
    follower = logData[sessionID]
    return followers_db.remove_follower(follower, followed)

def view_profile(data):
    if len(data) != 2:
        return "Invalid arguments"
    username, sessionID = data
    return users_db.view_profile(username)

def search(data):
    if len(data) != 2:
        return "Invalid arguments"
    pattern, sessionID = data
    return users_db.search(pattern)

def post_tweet(data):
    if len(data) < 2:
        return "Invalid arguments"
    sessionID = data[-1]
    if sessionID not in logData:
        return "Need to login first."
    len_d = len(data)                
    username, body = logData[sessionID], " ".join(data[: -1])
    return tweets_db.post_tweet(username,body)

def fetch_trending(data):
    return tweets_db.fetch_trending()

def connect_chat(data):
    if len(data) != 2:
        return "Invalid arguments"
    sendto, sessionID = data[0] ,data[1]
    if sendto not in toSessionID:
        return "the target is not online."
    sendtoport = toSessionID[sendto]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", int(sendtoport)+1024))
    sock.send(bytes("{} is chatting".format(logData[sessionID]),"utf-8"))
    sock.close()
    return "Chat invitation sent."

def send_msg(data):
    if len(data) < 3:
        return "Invalid arguments"
    sendto, message, sessionID = data[0], " ".join(data[1:-1]) ,data[-1]
    if sendto not in toSessionID:
        return "the target is not online."
    sendtoport = toSessionID[sendto]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", int(sendtoport)+1024))
    sock.send(bytes("{} :: {}".format(logData[sessionID],message),"utf-8"))
    sock.close()
    return "Message sent."

def fetch_updates(data):
    if len(data) not in [1, 3]:
        return "Invalid arguments"
    sessionID = data[-1]
    if sessionID not in logData:
        return "Need to login first"
    username = logData[sessionID]
    print(data, len(data))
    if len(data) == 3:
        if data[0]=="mark" and data[1]=="read":
            return updates_db.mark_read(username)
    return updates_db.fetch_updates(username)

def group_chat(data):
    sessionID = data[-1]
    if sessionID not in logData:
        return "Need to log in first"
    if len(data) < 3:
        return "Invalid arguments"
    username = logData[sessionID]
    groupname = data[0]
    msgBody = " ".join(data[1 : -1])
    membersList = groups_db.fetch_members(username, groupname, True)
    if not membersList:
        return "You are not member of the group"
    for targetUser in membersList:
        if targetUser not in toSessionID or targetUser == username:
            continue
        try:
            sendtoport = toSessionID[targetUser]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("localhost", int(sendtoport)+1024))
            sock.send(bytes("Group {} :: {}".format(groupname, msgBody),"utf-8"))
            sock.close()
        except:
            pass


def group(data):
    sessionID = data[-1]
    if len(data) < 2:
        return "Invalid arguments"
    if sessionID not in logData: # put in server
        return "Need to log in first"
    if data[0] not in ["create","add","remove","members","delete"]:
        return "Invalid command"
    username = logData[sessionID]
    groupname = data[1]
    if data[0] == "create":
        return groups_db.create_group(username,groupname)
    elif data[0] == "add":
        return groups_db.add_member(username,data[2:-1],groupname)
    elif data[0]=="remove":
        return groups_db.remove_member(username,data[2:-1],groupname)
    elif data[0]=="members":
        members =  groups_db.fetch_members(username,groupname)
        if not members:
            return "Does not have access to group members list"
        return "Members : " + " ".join(members)
    elif data[0]=="delete":
        return groups_db.remove_group(username,groupname)

def fetch_feed(data):
    sessionID, numTweets, numPage = data[-1], 5, 1
    if sessionID not in logData:
        return "Need to login first"
    username = logData[sessionID]
    if len(data) == 2:
        numTweets = int(data[0])
    elif len(data) == 3:
        numTweets, numPage = int(data[0]), int(data[1])
    elif len(data) > 3:
        return "Invalid arguments"
    tweets = tweets_db.fetch_feed(username, numTweets, numPage)
    return "".join(tweets)

def fetch_hashtag(data):
    numTweets, numPage = 5, 1
    hashtag = data[0]
    if len(data) == 3:
        numTweets = int(data[1])
    elif len(data) == 4:
        numTweets, numPage = int(data[1]), int(data[2])
    elif len(data) > 3:
        return "Invalid arguments"
    tweets = tweets_db.fetch_tweets_by_tag(hashtag, numTweets, numPage)
    return "".join(tweets)

def fetch_posts(data):
    numTweets, numPage = 5, 1
    if data[-1] not in logData:
        return "Login first to see posts"
    username = logData[data[-1]]
    if len(data) == 2:
        numTweets = int(data[0])
    elif len(data) == 3:
        numTweets, numPage = int(data[0]), int(data[1])
    elif len(data) > 3:
        return "Invalid arguments"
    tweets = tweets_db.fetch_posts(username, numTweets, numPage)
    return "".join(tweets)

def pin_tweet(data):
    if data[-1] not in logData:
        return "Login first to see posts"
    username = logData[data[-1]]
    if len(data)==2:
        tweet_id = int(data[0])
    else:
        return "Invalid arguments"
    if tweets_db.pin_tweet(username,tweet_id):
        return "Pin Successful"
    return "You have already pinned the tweet"
