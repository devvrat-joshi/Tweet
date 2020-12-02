"""
1. Tweet intensive
"""

import lorem
from random import randint, shuffle
numCommands = 1000

print("register tron002 s s")
for i in range(numCommands - 1):
    print("tweet")
    para = lorem.paragraph().split()
    numTags = randint(1, 10)
    leng = len(para)
    for h in range(numTags):
        j = randint(0, leng - 1)
        para[j] = "#" +para[j]
    numTags = randint(1, 5)
    for x in range(numTags):
        integer = randint(ord('a'), ord('z'))
        para.append('#' + chr(integer))
    shuffle(para)
    para = " ".join(para)
    print(para[:200])

    
        
    

