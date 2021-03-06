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
                # Delay Tweeting with sleep function. One tweet per hour will result in the bot tweeting for ~1 year(354.166.. days).
                # One tweet per hour(3600s* ~8500lines = 30,600,000s)
                # 30,600,000s / 84,600s/year = 354.166.. days
                sleep(3600)
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
            tweet_content = tweet_content + "#tomsawyer #bookbytweet"
            tweet(tweet_content)            
    else:
        pass

#Main
fileRead()
