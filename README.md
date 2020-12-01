<!-- TABLE OF CONTENTS -->
presentation, report, video

- HLD: Document detailing the networking paradigm. Handled Use cases. 
- LLD: Proposed structure of networking paradigm. 
- Client and Server side of the logic. 
- State management. 
- Commands and Action management. 
- Security aspects.
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">File Structure</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Dependencies</a></li>
        <li><a href="#prerequisites">Running the Files</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Dependencies
The following python modules needs to be additionally installed in order to run the files.
* pip3
  ```sh
  pip3 install colorama sqlite3
  ```
* [Mininet](http://mininet.org/download/)

### Running the Files
  
1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. In the home directory of the project, run the server program.
   ```sh
   python3 server.py
   ```
3. Run the client program
    ```sh
    python3 chat_client.py
    ```

### Running the tests
1. Change directory to ```mininet/```
   ```sh
   cd mininet
   ```
2. To run the testfiles, run ```make``` command.
   ```sh
   make 
   ```
3. Real-time server activity can be seen on the screen.
4. Access the text output files in ```mininet/tests/output/```

# Feature Checklist
### Basic Features:
✅ Register New User  
✅ Login  
✅ Get Updates  
✅ Logout  
✅ Search Registered Users  
✅ Follow/Unfollow Any User  
❌ Control Add/Delete Followers  
✅ Post Tweets  
✅ Categorize Tweets with Hashtags  

### Advanced Features
✅ Search and Display Tweets Under Specific Hashtags  
✅ Fetch List of Online Followers  
✅ Initiate Chat Session with Followers  
✅ Retweet Tweets  
✅ Scale Server to Handle Multiple Requests  
❌ Multiple Instances of Server  

### Security Features
✅ User Authenticate With Server to Access Features  
✅ Obscured Password Input  

### Bonus Features
✅ Pin Tweets To The Profile  
✅ Anyone Can View The Profile and The Pinned Tweets  
✅ Create Groups  
✅ Add/Remove Members From a Group  
✅ Check Group Owner/Admin and Members  
✅ Broadcast A Message To All The Members Of Group  
✅ Delete Group  
✅ Attractive Interface  

### Extra Features
✅ Get Notification  
- If Someone Mentions You In Their Tweet  
- If your Tweet is Retweeted   


# Commands
### Login 🔒
```Syntax: login <username>```  
Then the terminal prompts for the password.

### Register
```Syntax: register <username>```  
Then the terminal prompts for the password and re-typing the password.

### Logout
```Syntax: logout```  
Logout the current session of the user that is currently logged in.


### Follow
```Syntax: follow <username_to_follow>```  
To start following someone with the given username. The tweets posted by that user would appear in our feed.

### Unfollow
```Syntax: search <username_to_unfollow>```  
To start unfollowing someone

### Search
```Syntax: search <username_pattern>```  
To search the registered usernames which matches with the given pattern as *prefix*.

### Profile
```Syntax: profile <target_username>```  
View profile of the given username. In a user's profile, we can see
- number of followers
- the number of users he/she is following 
- pinned tweets. 

### Tweet
```Syntax: tweet``` 
Opens a text editor (nano). Once done, save (Ctrl + S) and exit the text editor. Mini-Tweet then asks for a confirmation once done, before finally posting the tweet.

### Posts
```Syntax: posts <tweets_per_page = 5>  <page_number = 1>```  
To view the latest personal tweets posted by the user that is currently logged in.
- tweets_per_page (default = 5) are the number of tweets that will be visible in a single page.
- page_number (default = 1) is used to switch to a different page.



### Trending
```Syntax: trending```  
Get the top 5 trending hashtags in the last 24 hours along with the count of each.


### Hashtag
```Syntax: hashtag <hashtag_name> <tweets_per_page> <page_number>```  
To view the latest tweets of a particular hashtag. 
- tweets_per_page (default = 5) are the number of tweets that will be visible in a single page.
- page_number (default = 1) is used to switch to a different page.


### Feed
```Syntax: feed <tweets_per_page> <page_number> ```
To view the personalised feed which includes the latest tweets of the profiles you are following.
- tweets_per_page (default = 5) are the number of tweets that will be visible in a single page.
- page_number (default = 1) is used to switch to a different page.

### Pin
```Syntax: pin <tweet_id>```  
To pin a to your profile, give the tweet_id as an argument to pin that particular tweet. The pinned tweet will be visible in the user's profile.

### Retweet
```Syntax: retweet <tweet_id>```  
To retweet a given tweet, give the tweet_id as an argument and the tweet will be retweeted with your username.


### Online
```Syntax: online <followers_per_page> <page_number>```  
To get the list of all online followers.
- followers_per_page (default = 8) are the number of tweets that will be visible in a single page.
- page_number (default = 1) is used to switch to a different page.

### Chat
```Syntax: msg <target_user> [message_statement]```  
Sends the chat message_statement to the target_user from the current online

### Manage Group

#### Create Group
```Syntax: group create <group_name>```
Create a group of group_name with the current online user as the admin/owner.

#### Add Group Members
```Syntax: group add <group_name> <add_member1> [<add_member2> <add_member3> ...] ```
Adds the list of given usernames in the group_name. The current user must be group owner to execute this command.

#### Remove Group Members
```Syntax: group add <group_name> <add_member1> [<add_member2> <add_member3> ...] ```
Removes the list of given usernames from the group_name. The current user must be group owner to execute this command.

#### Fetch Group Members List
```Syntax: group members <group_name>```
Fetches the list of members for the group_name. The current user must be a member of the group.

#### Delete Group
```Syntax: group delete <group_name>```
Deletes the entire group_name. The current user must be group owner to execute this command.

### Group Chat
```Syntax: stream <group_name> [msg_statement]```
To send the msg_statement to the group members. The current user must be group member to send messages in group chat.


## Client and Server Side Logic
### Server Side Logic
- Server is a multi-threaded concurrent server, which can handle around 4500 queries per minute.
- Whenever server receives a query, it checks the first word of the query.
- The server creates a new thread per query.
- The first word is the command which client is asking the server to execute.
- Server will look into the dictionary of commands and if the command is present in the list, then there will be an entry of a function corresponding to that command.
- Server will run that function and pass the data from the client as argument.
- The state maintanance and database design is under the topic, HLD, LLD.

### Client Side Logic

- When client program starts, it sends to server a command named "init".
- Server will return a token number to that client which will be stored by client for the future use.
- For every input command from the user, client opens a TCP connection with the server and also sends this token number so that the server can maintain a state of this particular client.
- The client program also starts a server on its side, so that if the main server receives a chat message that is to be send to the client, then it can connect to the server at client side.
- Client program gives an input for the user, from where user can enter all the commands that are to be executed by the server.
- First the user has to enter the credentials and then the server will map the token number of that client to the username of that client after authentication is successful.
- If a tweet is to be sent, then client program will open nano editor.
- User types the tweet in this editor and after pressing "Y", the tweet will be posted with the credentials of client.



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_


## State Management
###

## Security Aspects


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)
