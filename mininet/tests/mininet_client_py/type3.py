"""
1. Updates
2. Tweet
3. Feed intensive process.
"""
import lorem
from random import randint, shuffle
numCommands = 1000

print("register tron004 s s")
print("follow tron001")
print("follow tron002")
print("follow tron000")

for i in range(numCommands):
    command = randint(1, 3)
    if command == 2:
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

    elif command == 1:
        print("updates")
        print("updates mark read")
    else:
        print("feed")

