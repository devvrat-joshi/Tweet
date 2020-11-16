import users_db
tokenCounter = 1
logData = {}

def init(data):
    global tokenCounter
    tokenCounter += 1
    return str(tokenCounter)

def login(data):
    print(len(data),data)
    if len(data) != 3:
        return "Invalid arguments"
    username, password,sessionID = data
    print(username,password,sessionID)
    if sessionID in logData:
        return "Already logged in!"
    if db.login(username,password):
        logData[sessionID] = username
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
    elif db.register(username, password):
        logData[sessionID] = username
        return "Welcome to the mini-tweet team, " + username + " !!!"
    else:
        return "User already exists"

def logout(data):
    if len(data) != 1:
        return "Invalid arguments"
    sessionID = data[0]
    if sessionID not in logData:
        return "Need to first login!"
    else:
        logData.pop(sessionID)
        return "$Logged_out$"

def search_user(data):
    if len(data) != 3:
        return "Invalid arguments"
    usernameRegex, sessionID = data
    if sessionID in logData:
        return "Need to be logged in first"
    if 