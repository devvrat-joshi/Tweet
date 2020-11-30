""" These are the command which do not require login
1. search <regex>
2. profile <username>
3. trending
4. hashtag
"""
from random import *
numCommands = 1000

for i in range(numCommands):
    command = randint(1, 4)
    if command == 3:
        print("trending")
    elif command == 2:
        keys = ["tron", "tron0", "tron01", "tron1", "tron1", "tron00000", "tron2", "tron9"]
        j = randint(0, len(keys) - 1)
        print("search", keys[j])
    elif command == 2:
        suffix = str(i)
        while len(suffix) < 3:
            suffix = "0" + suffix
        body = "tron" + suffix
        print("profile", body)
    else:
        integer = randint(ord('a'), ord('z'))
        tag = chr(integer)
        print("hashtag", tag)


