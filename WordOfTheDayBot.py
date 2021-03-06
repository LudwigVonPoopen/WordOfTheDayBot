import praw
import config
import urllib.request as urllib2
from bs4 import BeautifulSoup

dict = "http://www.dictionary.com/wordoftheday/"

page = urllib2.urlopen(dict)

soup = BeautifulSoup(page, 'html.parser')

word = soup.title.string

word = word.replace("Get the Word of the Day - ", "")
word = word.replace(" | Dictionary.com", "")

definition = soup.ol.li

definition_str = str(definition)

x = definition_str.index("<span>")
y = definition_str.index("<", x+1)

definition_str = definition_str[x+6:y]

post_text = word + ": " + definition_str

reddit = praw.Reddit(username = config.username,
                     password = config.password,
                     client_id = config.client_id,
                     client_secret = config.client_secret,
                     user_agent = config.user_agent)

subreddit = reddit.subreddit("pythonforengineers")

subreddit.submit(title="Word of the Day", selftext=post_text, send_replies=False)
print("Post Submitted")


reddit = praw.Reddit(username = config.username,
                     password = config.password,
                     client_id = config.client_id,
                     client_secret = config.client_secret,
                     user_agent = config.user_agent)

subreddit = reddit.subreddit("pythonforengineers")

subreddit.submit(title="Word of the Day", selftext=post_text, send_replies=False)
print("Post Submitted")
