oo = """
<HMTL>
<HEAD>
<TITLE>webpage1</TITLE>
</HEAD>
<BODY BGCOLOR="FFFFFf" LINK="006666" ALINK="8B4513" VLINK="006666">
<TABLE WIDTH="75%" ALIGN="center">
<TR>
<TD>
<DIV ALIGN="center"><H1>STARTING . . . </H1></DIV>


<DIV ALIGN="justify"><P>There are lots of ways to create web pages using already coded programmes. These lessons will teach you how to use the underlying HyperText Markup Language -  HTML. 
<BR>
<P>HTML isn't computer code, but is a language that uses US English to enable texts (words, images, sounds) to be inserted and formatting such as colo(u)r and centre/ering to be written in. The process is fairly simple; the main difficulties often lie in small mistakes - if you slip up while word processing your reader may pick up your typos, but the page will still be legible. However, if your HTML is inaccurate the page may not appear - writing web pages is, at the least, very good practice for proof reading!</P>

<P>Learning HTML will enable you to:
<UL>
<LI>create your own simple pages
<LI>read and appreciate pages created by others
<LI>develop an understanding of the creative and literary implications of web-texts
<LI>have the confidence to branch out into more complex web design 
</UL></P>

<P>A HTML web page is made up of tags. Tags are placed in brackets like this <B>< tag > </B>. A tag tells the browser how to display information. Most tags need to be opened < tag > and closed < /tag >.

<P> To make a simple web page you need to know only four tags:
<UL>
<LI>< HTML > tells the browser your page is written in HTML format
<LI>< HEAD > this is a kind of preface of vital information that doesn't appear on the screen. 
<LI>< TITLE >Write the title of the web page here - this is the information that viewers see on the upper bar of their screen. (I've given this page the title 'webpage1').
<LI>< BODY >This is where you put the content of your page, the words and pictures that people read on the screen. 
</UL>
<P>All these tags need to be closed.

<H4>EXERCISE</H4>

<P>Write a simple web page.</P>
<P> Copy out exactly the HTML below, using a WP program such as Notepad.<BR>
Information in <I>italics</I> indicates where you can insert your own text, other information is HTML and needs to be exact. However, make sure there are no spaces between the tag brackets and the text inside.<BR>
(Find Notepad by going to the START menu\ PROGRAMS\ ACCESSORIES\ NOTEPAD). 
<P>
< HTML ><BR>
< HEAD ><BR>
< TITLE ><I> title of page</I>< /TITLE ><BR>
< /HEAD ><BR>
< BODY><BR>
<I> write what you like here: 'my first web page', or a piece about what you are reading, or a few thoughts on the course, or copy out a few words from a book or cornflake packet.  Just type in your words using no extras such as bold, or italics, as these have special HTML tags, although you may use upper and lower case letters and single spaces. </I><BR>

< /BODY ><BR>
< /HTML ><BR>

<P>Save the file as 'first.html' (ie. call the file anything at all) It's useful if you start a folder - just as you would for word-processing - and call it something like WEBPAGES, and put your first.html file in the folder.

<P>NOW - open your browser.<BR>
On Netscape the process is: <BR>  
Top menu; FILE\ OPEN PAGE\ CHOOSE FILE<BR> 
Click on your WEBPAGES folder\ FIRST file<BR>
Click 'open' and your page should appear.
<P>On Internet Explorer: <BR>
Top menu; FILE\ OPEN\ BROWSE <BR> 
Click on your WEBPAGES folder\ FIRST file<BR>
Click 'open' and your page should appear.<BR>


<P>If the page doesn't open, go back over your notepad typing and make sure that all the HTML tags are correct. Check there are no spaces between tags and internal text; check that all tags are closed; check that you haven't written < HTLM > or < BDDY >.  Your page will work eventually. 
<P>
Make another page. Call it somethingdifferent.html and place it in the same WEBPAGES folder as detailed above.
<P>start formatting in <A HREF="webpage2.html">lesson two</A>
<BR><A HREF="col3.html">back to wws index</A> </P>
</P>
 
  
</DIV>


</TD>
</TR>
</TABLE>
</BODY>
</HTML>







"""

avatar = """
HTTP/1.1 200 OK\nDate: Tue, 18 Aug 2015 15:44:04 GMT\nServer: Apache/2.2.3 (CentOS)
Content-Type: text/html\n
<style>
/* Bordered form */
form {
  border: 3px solid #f1f1f1;
}

/* Full-width inputs */
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

/* Set a style for all buttons */
button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

/* Add a hover effect for buttons */
button:hover {
  opacity: 0.8;
}

/* Extra style for the cancel button (red) */
.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

/* Center the avatar image inside this container */
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

/* Avatar image */
img.avatar {
  width: 40%;
  border-radius: 50%;
}

/* Add padding to containers */
.container {
  padding: 16px;
}

/* The "Forgot password" text */
span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
    display: block;
    float: none;
  }
  .cancelbtn {
    width: 100%;
  }
}
</style>
<form action="action_page.php" method="post">
  <div class="imgcontainer">
    <img src="image" style="width: 30%;height: auto;">
  </div>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>
"""
with open("inspire0.png", "r+b") as image_file:
  data = image_file.read()
  HTTP_RESPONSE = b'\r\n'.join([
      b"HTTP/1.1 200 OK",
      b"Connection: close",
      b"Content-Type: image/png",
      bytes("Content-Length: %s" % len(data),'utf-8'),
      b'', data 
  ] )
# print(HTTP_RESPONSE)