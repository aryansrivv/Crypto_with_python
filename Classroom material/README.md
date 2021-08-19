# JULY 8

Hello everyone and welcome to this course. This week, we're gonna be focussing on Cryptography with python. To start things off, you are gonna be needing a Python environment.
there are two ways to go about it: 
1)install python on your system - https://www.javatpoint.com/how-to-install-python
2)use online notebooks like google colab


Now moving forward with this week's material:
If you're completely new to cryptography, I would suggest going through these links first-
https://www.edureka.co/blog/what-is-cryptography/
and then go through the pages in this link to get familiar with different terms used in cryptography.
https://www.tutorialspoint.com/cryptography/index.htm 


Don't worry if you don't understand something on the first try, there are enough resources on the internet to keep you going and also keep posting your doubts on classroom or in the Whatsapp group. We are all here to help you out.
Try to complete the material by Saturday and of course, take care and have great learning ahead!

Python tutorial for beginners - https://www.tutorialspoint.com/python/python_quick_guide.htm


# JULY 10

Now, onwards with implementation of cryptographic techniques with python, go through pages in this link one by one:
https://www.tutorialspoint.com/cryptography_with_python/index.htm
Most of the code is pretty intuitive but if you have any doubts, do post it on the group.
Try to complete it by Thursday.


# JULY 16


Hey guys, So this week we will be learning about Sockets and Web Scraping.

You will be utilizing the first half of this week for learning Socket Programming in Python or Python-nmap module and using it to build a Port Scanner.

An excellent tutorial for Socket Programming can be found here https://yasoob.me/2013/08/06/python-socket-network-programming/.

You can read through this medium article - https://medium.com/manishmshiva/nmap-a-guide-to-the-greatest-scanning-tool-of-all-time-3bd1a973a5e5 , to learn about Nmap and how to use it. Then you can then use the python-nmap module linked here - https://pypi.org/project/python-nmap/  to create your own custom Port Scanner based on Nmap.


You can use either Socket Programming or the python-nmap module to create the port scanner.





# JULY 20


Hey Guys,

So for the next half of this week, you'll be learning about Python's requests and BeautifulSoup library for web scraping. 
Attached below are some tutorial videos to get you started.
https://www.youtube.com/watch?v=tb8gHvYlCFs
https://www.youtube.com/watch?v=a6fIbtFB46g
https://www.youtube.com/watch?v=ng2o98k983k
https://www.youtube.com/watch?v=yqm6MBt-yfY (Optional but highly recommended)


I am expecting everyone of you to have gone through these videos by 23rd of July.




# JULY 24


Hey Guys,

You will be utilizing the rest of this week to learn about Web Crawlers, Web Scraping with Scrapy and how to store the scraped data in a database.
Traversy Media's video linked here: https://www.youtube.com/watch?v=ALizgnSFTwQ , provides an excellent tutorial to the topic.
You can follow this tutorial here: https://realpython.com/web-scraping-with-scrapy-and-mongodb/ , which will teach you about how to store scraped data in your db. You can setup a local MongoDB database or use their MongoDB Atlas Cloud Database (https://www.mongodb.com/cloud/atlas) to setup a free database hosted in the cloud.



# JULY 27


Hey everyone!
Hopefully everyone's done with web crawling, this time you'll be learning about OWASP top 10.
(https://owasp.org/www-project-top-ten/).
We won't be covering all of them as some of them are self explanatory. We'll be starting with #1 vulnerability i.e Injection.

SQL, NOSQL and LDAP injection have been considered as one of the most notorious vulnerabilities out there and some websites still have them. Here's something to get you started with.

SQL Basics for Beginners (edureka!):

https://www.youtube.com/watch?v=zbMHLJ0dY4w

You can go through it 1.5x or 2x, just try to get an understanding of how SQL works.

To help you get a better understanding of sql injection:

Running an SQL Injection Attack (Computerphile):

https://www.youtube.com/watch?v=ciNHn38EyRc

A few sqli challenges:

Try doing the first 2 labs from https://portswigger.net/web-security/sql-injection without using burpsuite .
You can also read through the material there for a better understanding.


Also, instead of manually entering the payload through the browser try to use python and send the payload (for the 1st two labs from portswigger)



# JULY 30


Hey everyone!

Today, let's start off with XSS (Cross-Site Scripting). XSS occurs when an HTML input is not properly sanitized, allowing scripting (generally JavaScript) to be executed when entered in that input. Hackers can leverage this vulnerability to execute malicious scripts. XSS is of three types:

Reflected XSS: This happens when the attacker injects browser executable code that affects non-persistent data. This type of attack isn't stored on servers, hence it requires some user interaction (like clicking on a link).

Stored XSS: This is a more damaging vulnerability. The malicious code is injected directly into the server, thus compromising the integrity of the web application itself.

DOM based XSS: DOM or Document Object Model is a programming interface between HTML and JS that allows web apps to update dynamically, and includes functions like eval() or window.location. These functions allow dynamic code execution, so if a hacker can gain control to an input to one of such function, he can use it to sneak in malicious code.

Here's some material for you to get started:

Videos:
Cross Site Scripting (Computerphile):
https://www.youtube.com/watch?v=L5l9lSnNMxg

XXS (PwnFunction):

https://www.youtube.com/watch?v=EoaDgUgS6QA


Reading:
https://portswigger.net/web-security/cross-site-scripting

Labs to Solve:

How many ever labs you can from: https://xss.pwnfunction.com/

How many ever labs you can from: https://unescape-room.jobertabma.nl/



# August 3 
Hey guys hope you're done with web scraping, SQLi & XSS. This assignment is based on it.



(Web Scraping):

List out all the href links, names of artists, categories from the website.



(Web Security):

Test for XSS and SQLi on http://testphp.vulnweb.com/ using python.
You can hardcode 2 to 3 payloads for each vulnerability and test it against the website (use the response to detect for XSS or SQLi).



Please don't plagiarize your code



Submit the code as .py file.


# August 7 

Cryptography with python assignment:

Go to this site https://cryptopals.com/sets/1 and submit the code of the first 5 questions. Make sure to properly comment on your code in your own words.
You can either submit the individual .py files or a txt or a word document containing all the codes.


# August 20 

FINAL QUIZ 
<img width="1440" alt="Screenshot 2021-08-19 at 11 12 12 PM" src="https://user-images.githubusercontent.com/74819332/130151317-8fff5d3f-2ee2-40be-a011-b98994b397ba.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 12 22 PM" src="https://user-images.githubusercontent.com/74819332/130151319-42ae1c2f-e7fc-43c7-ab86-80245e59d641.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 12 29 PM" src="https://user-images.githubusercontent.com/74819332/130151318-8c389739-d153-458a-ad8f-508e8f6c3110.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 13 26 PM" src="https://user-images.githubusercontent.com/74819332/130151322-6357701a-3dea-4851-a9a2-bfc3b8ddbaa7.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 13 24 PM" src="https://user-images.githubusercontent.com/74819332/130151320-83c303a6-8fad-4770-b228-fc39597eaa47.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 13 21 PM" src="https://user-images.githubusercontent.com/74819332/130151316-242e2bc8-b631-40b8-9d9f-429803319232.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 13 17 PM" src="https://user-images.githubusercontent.com/74819332/130151314-db5ea9d3-261a-4434-a145-3f9358d13c3c.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 12 54 PM" src="https://user-images.githubusercontent.com/74819332/130151321-31e5cb7a-5b7c-4784-875f-4c6e26074e11.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 12 46 PM" src="https://user-images.githubusercontent.com/74819332/130151315-7d8183ee-c22a-433f-a50b-7ee774619051.png">
<img width="1440" alt="Screenshot 2021-08-19 at 11 12 40 PM" src="https://user-images.githubusercontent.com/74819332/130151323-673221b4-5079-4fbd-96e3-4304d4403899.png">

