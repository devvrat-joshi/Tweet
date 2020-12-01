"""
Here we extract the data from the command arguments and using the Database utility functions in other files, it finally executes the given commands
"""

from . import users_db,followers_db,tweets_db, updates_db, groups_db
from colorama import init, Fore, Back, Style
import socket
tokenCounter = 1
#dictionaries to map sessionID to username and vice versa as well
logData = {}
toSessionID = {}

#runs when a client connects to the server socket
def init(data):
    #assign new sessionID to each new client
    global tokenCounter
    tokenCounter += 1
    return str(tokenCounter)

#when client attempts login
def login(data):
    if len(data) != 3:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    username, password,sessionID = data
    if sessionID in logData:
        return Fore.BLUE + "Already logged in!" + Fore.WHITE
    if users_db.login(username,password):
        logData[sessionID] = username
        toSessionID[username] = sessionID
        return Fore.GREEN + "Logged in Successfully!" + Fore.WHITE
    return Fore.RED + "Invalid Username/Password" + Fore.WHITE

#when a username is attempted to be registered
def register(data):
    if len(data) != 4:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    username, password, repassword, sessionID = data
    if sessionID in logData:
        return Fore.BLUE + "Already logged in!" + Fore.WHITE
    elif password != repassword:
        return Fore.RED + "Password doesn't match" + Fore.WHITE
    elif users_db.register(username, password):
        logData[sessionID] = username
        toSessionID[username] = sessionID
        return Fore.GREEN + "Welcome to the mini-tweet team, " + Fore.BLUE + username + Fore.WHITE + " !!!" + Fore.WHITE
    else:
        return Fore.RED + "User already exists" + Fore.WHITE

#logout the username
def logout(data):
    if len(data) != 1:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    sessionID = data[0]
    if sessionID not in logData:
        return Fore.RED + "Need to be logged in first." + Fore.WHITE
    else:
        if users_db.logout(logData[sessionID]):
            toSessionID.pop(logData[sessionID])
            logData.pop(sessionID)
            return Fore.GREEN + "$Logged_out$" + Fore.WHITE
        else:
            return Fore.RED + "Cannot logout" + Fore.WHITE

def add_follower(data):
    if len(data) != 2:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    followed, sessionID = data
    if sessionID not in logData:
        return Fore.RED + "Need to login first" + Fore.WHITE
    follower = logData[sessionID]
    return followers_db.add_follower(follower, followed)

def remove_follower(data):
    if len(data) != 2:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    followed, sessionID = data
    if sessionID not in logData:
        return Fore.RED + "Need to login first" + Fore.WHITE
    follower = logData[sessionID]
    return followers_db.remove_follower(follower, followed)

#views the profile of username
def view_profile(data):
    if len(data) != 2:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    username, sessionID = data
    return users_db.view_profile(username)

#search for a username
def search(data):
    if len(data) != 2:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    pattern, sessionID = data
    return users_db.search(pattern)

def post_tweet(data):
    if len(data) < 2:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    sessionID = data[-1]
    if sessionID not in logData:
        return Fore.RED + "Need to login first." + Fore.WHITE             
    username, body = logData[sessionID], " ".join(data[: -1])
    return tweets_db.post_tweet(username,body)

#fetch the trending hashtags
def fetch_trending(data):
    return tweets_db.fetch_trending()

#for 1to1 chat message
def send_msg(data):
    if len(data) < 3:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    if data[-1] not in logData:
        return Fore.RED + "Need to login first" + Fore.WHITE
    sendto, message, sessionID = data[0], " ".join(data[1:-1]) ,data[-1]
    is_follower = followers_db.is_follower(logData[sessionID], sendto)
    if not is_follower:
        return Fore.RED + "Can only chat with followers" + Fore.WHITE
    if sendto not in toSessionID:
        return Fore.GREEN +  "the target is not online." + Fore.WHITE
    #now Main-server attempts to connect to the chat-server at client side
    sendtoport = toSessionID[sendto]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", int(sendtoport)+1024))
    sock.send(bytes(Fore.CYAN +logData[sessionID] + Fore.WHITE + " :: {}".format(message),"utf-8"))
    sock.close()
    return Fore.GREEN + "Message sent." + Fore.WHITE

#fetch the updates for the given username
def fetch_updates(data):
    if len(data) not in [1, 3]:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    sessionID = data[-1]
    if sessionID not in logData:
        return Fore.RED + "Need to login first" + Fore.WHITE
    username = logData[sessionID]
    print(data, len(data))
    if len(data) == 3:
        if data[0]=="mark" and data[1]=="read":
            return updates_db.mark_read(username)
    return updates_db.fetch_updates(username)

#to send the message in a group
def group_chat(data):
    sessionID = data[-1]
    if sessionID not in logData:
        return Fore.RED + "Need to log in first" + Fore.WHITE
    if len(data) < 3:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    username = logData[sessionID]
    groupname = data[0]
    msgBody = " ".join(data[1 : -1])
    membersList = groups_db.fetch_members(username, groupname, True)
    if not membersList:
        return Fore.RED + "You are not member of the group" + Fore.WHITE
    #for every member
    for targetUser in membersList:
        #leave the offline users and the original sender
        if targetUser not in toSessionID or targetUser == username:
            continue
        try:
            #send the message to the chat-servers on the clients
            sendtoport = toSessionID[targetUser]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("localhost", int(sendtoport)+1024))
            sock.send(bytes("Group " + Fore.CYAN + groupname + Fore.WHITE + " :: " + Fore.CYAN + username + Fore.WHITE + " " + msgBody,"utf-8"))
            sock.close()
        except:
            pass

#group management :add members, remove members, create, delete
def group(data):
    sessionID = data[-1]
    if len(data) < 2:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    if sessionID not in logData: # put in server
        return Fore.RED + "Need to log in first" + Fore.WHITE
    if data[0] not in ["create","add","remove","members","delete"]:
        return Fore.RED + "Invalid command" + Fore.WHITE
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
            return Fore.RED + "Does not have access to group members list" + Fore.WHITE
        return "Members : " + " ".join(members)
    elif data[0]=="delete":
        return groups_db.remove_group(username,groupname)

#generate feed for the given user
def fetch_feed(data):
    sessionID, numTweets, numPage = data[-1], 5, 1
    if sessionID not in logData:
        return Fore.RED + "Need to login first" + Fore.WHITE
    username = logData[sessionID]
    if len(data) == 2:
        numTweets = int(data[0])
    elif len(data) == 3:
        numTweets, numPage = int(data[0]), int(data[1])
    elif len(data) > 3:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    tweets = tweets_db.fetch_feed(username, numTweets, numPage)
    return "".join(tweets)

#fetch the tweets with the given hashtag
def fetch_hashtag(data):
    numTweets, numPage = 5, 1
    hashtag = data[0]
    if len(data) == 3:
        numTweets = int(data[1])
    elif len(data) == 4:
        numTweets, numPage = int(data[1]), int(data[2])
    elif len(data) > 3:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    tweets = tweets_db.fetch_tweets_by_tag(hashtag, numTweets, numPage)
    return "".join(tweets)

#fetch the tweets posted by the current logged in users
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
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    tweets = tweets_db.fetch_posts(username, numTweets, numPage)
    return "".join(tweets)

#pin a tweet to profile
def pin_tweet(data):
    if data[-1] not in logData:
        return Fore.RED + "Login first to see posts" + Fore.WHITE
    username = logData[data[-1]]
    if len(data)==2:
        tweet_id = int(data[0])
    else:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    if tweets_db.pin_tweet(username,tweet_id):
        return Fore.GREEN + "Pin Successful" + Fore.WHITE
    return Fore.BLUE + "You have already pinned the tweet" + Fore.WHITE

def retweet_id(data):
    if data[-1] not in logData:
        return Fore.RED + "Need to login first." + Fore.WHITE
    username = logData[data[-1]]
    if len(data)==2:
        tweet_id = int(data[0])
    else:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    return tweets_db.retweet_id(username,tweet_id)

#fetch the list of online followers
def fetch_online(data):
    sessionID, numFollowers, numPage = data[-1], 5, 1
    if sessionID not in logData:
        return Fore.RED + "Need to login first" + Fore.WHITE
    username = logData[sessionID]
    if len(data) == 2:
        numFollowers = int(data[0])
    elif len(data) == 3:
        numFollowers, numPage = int(data[0]), int(data[1])
    elif len(data) > 3:
        return Fore.RED + "Invalid arguments" + Fore.WHITE
    online_followers = []
    followers = followers_db.fetch_online(username)
    for member in followers:
        if member in toSessionID:
            online_followers.append(Fore.GREEN + "*" + Fore.WHITE + member)
    s,e  = ( numPage - 1) * numFollowers , numPage * numFollowers
    return ("\n").join(online_followers[s : e])
        
