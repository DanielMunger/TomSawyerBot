#imports
import tweepy
from time import sleep
from credentials import *

#Set up OAuth amd integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Open and read Tom Sawyer file
tom_file = open('TomSawyer.txt', 'r')
tom_lines = tom_file.readlines()
tom_file.close()

#Tweet Functions
def fileRead():
    for line in tom_lines:
        try:
            if line != '\n':
                contentCheck(line)

            else:
                pass
        except tweepy.TweepError as error:
            print(error.reason)

def tweet(tweet):
    api.update_status(tweet)

def contentCheck(tweet_content):
    if tweet_content:
        tweet_length = len(tweet_content)
        if tweet_length > 2:
            print(tweet_content)
            
    #Need an error catch here else:

fileRead()
