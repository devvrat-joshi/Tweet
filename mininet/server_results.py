import curses, time
import logging as log
log.basicConfig(
    filename="logs.txt", filemode="a", level=log.INFO,
)


total = "Total Queries Served: "

commands = {
    "init     : ":0,
    "login    : ":0,
    "register : ":0,
    "logout   : ":0,
    "follow   : ":0,
    "unfollow : ":0,
    "profile  : ":0,
    "search   : ":0,
    "tweet    : ":0,
    "trending : ":0,
    "chat    : ": 0,
    "msg     : ": 0,
    "updates : ": 0,
    "group   : ": 0,
    "stream  : ": 0,
    "feed    : ": 0,
    "hashtag : ": 0,
    "posts   : ": 0,
    "pin     : " : 0,
    "retweet : " : 0,
    "online  : " : 0
}

cmd = {
    "init":0,
    "login":0,
    "register":0,
    "logout":0,
    "follow":0,
    "unfollow":0,
    "profile":0,
    "search":0,
    "tweet":0,
    "trending":0,
    "chat": 0,
    "msg": 0,
    "updates": 0,
    "group": 0,
    "stream": 0,
    "feed": 0,
    "hashtag": 0,
    "posts": 0,
    "pin" : 0,
    "retweet" : 0,
    "online" : 0
}
new_file = open("results.csv","w")
file = open("tests/output/server.txt","r")
def main(stdscr):
    global total
    curses.curs_set(0)
    curses.init_pair(3, 3, 55)
    stdscr.bkgd(' ', curses.color_pair(3)|curses.A_BOLD)
    curses.init_pair(8,curses.COLOR_WHITE, 18)
    h,w = stdscr.getmaxyx()
    stdscr.addstr(0,0," "*w,curses.color_pair(8))
    stdscr.addstr(0,(w-len(total))//2,total,curses.color_pair(8))
    x = list(commands.keys())
    a = list(cmd.keys())
    time.sleep(5)
    start = time.time()
    for i in range(10):
        stdscr.addstr(2+i*2,5,x[i],curses.color_pair(3))
    for i in range(10,20):
        stdscr.addstr(2+(i-10)*2,w//2+3,x[i],curses.color_pair(3))
    stdscr.refresh()
    while 1:
        y = " "
        while y:
            y = file.readline()
            for i in range(21):
                # log.info(y)
                if y.find(a[i])!=-1:
                    commands[x[i]]+=1
                    break
            # log.info(commands)
        tnm = str(int(time.time()-start))
        tm = "time in seconds : " + tnm
        tot = sum(list(commands.values()))
        total = "Total Queries Served: {}".format(tot)
        if tot:
            new_file.write("{},{}\n".format(time.time()-start,tot))
        stdscr.addstr(0,(w-len(total))//2,total,curses.color_pair(8))
        stdscr.addstr(0,w-len(tm)-2,tm,curses.color_pair(8))
        for i in range(10):
            stdscr.addstr(2+i*2,5,x[i]+str(commands[x[i]]),curses.color_pair(3))
        for i in range(10,20):
            stdscr.addstr(2+(i-10)*2,w//2+3,x[i]+str(commands[x[i]]),curses.color_pair(3))
        stdscr.refresh()
        # exit()
print(len(commands))
curses.wrapper(main)
