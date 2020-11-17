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
    "trending": views.fetch_trending
}