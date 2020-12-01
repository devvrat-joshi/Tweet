<!-- TABLE OF CONTENTS -->
presentation, report, video
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
3. Real-time server activity can be seen on the screen
4. Access the text output files in ```mininet/tests/output/```

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
To search the registered usernames which matches with the given pattern as **prefix**.

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
- tweets_per_page (default = 5), are the number of tweets that will be visible at once.
- page_number (default = 1), is used to switch to the next page or previous page, to move through the 
To get personal tweets with numTweets_per_page is the number of tweets that are to be fetched per page, and page_number is the page number of the above mentioned scheme. Default value of numTweets_per_page is 5 and page_number is 1 if they are not given as argument to the command.



### Trending
```Syntax: trending```  
Get the top 5 trending hashtags in the last 24 hours along with the count of each.


### Hashtag
```Syntax: hashtag <hashtag_name> <tweets_per_page> <page_number>```  
To view the tweets of a particular hashtag. The number of tweets per page can be given as argument by tweets_per_page and the page number can be given by page_number. The default tweets per page is 5 and page_number is 1.


### Feed
```Syntax: feed <tweets_per_page> <page_number> ```
To get the personalised feed which includes the tweets of the profiles whom you are following. The number of tweets per page can be given as argument by tweets_per_page and the page number can be given by page_number. The default tweets per page is 5 and page_number is 1.

### Pin
```Syntax: pin <tweet_id>```  
To pin the tweet to your profile, give the tweet_id as an argument to pin that particular tweet.

### Retweet
```Syntax: retweet <tweet_id>```  
To retweet a tweet, give the tweet_id as an argument and and the tweet will be retweeted with your username.


### Online
```Syntax: online```  
To get the list of all online followers.

### Chat
```Syntax: online```  


### Group


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



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
