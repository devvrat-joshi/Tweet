"""
1. Register 200 users and then retweet
"""

from random import randint
numQuery = 200
for i in range(numQuery):
    print("register mutron" + "0"*(3-len(str(i))) + str(i) + " s s")
    for i in range(5):
        retweet_id = randint(1, 100)
        print("retweet "+str(retweet_id))
    print("logout")
