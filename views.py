import users_db,followers_db,tweets_db
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