import views
functions = {
    "init":views.init,
    "login":views.login,
    "register":views.register,
    "logout":views.logout,
    "follow":views.add_follower,
    "unfollow":views.remove_follower,
    "profile":views.view_profile,
    "search":views.search,
    "tweet":views.post_tweet,
    "trending": views.fetch_trending,
    "chat": views.connect_chat,
    "msg": views.send_msg,
    "updates": views.fetch_updates,
    "group": views.group,
    "stream": views.group_chat,
    "feed": views.fetch_feed,
    "hashtag": views.fetch_hashtag,
    "posts": views.fetch_posts,
    "pin" : views.pin_tweet
}