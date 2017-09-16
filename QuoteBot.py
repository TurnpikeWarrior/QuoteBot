# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "Bwf7N8YQVS3TRS8lQ39PPszlA"
consumer_secret = "SmeBFLyycX9aWN0LxnZbB7DZ9y7CYCHT5DpZsE3LE4prSFrnOK"
access_token = "14565141-wpps87otP8YFjQE2c7MuIaNyw09Bu1hm7u06k78HT"
access_token_secret = "HpraKAFI3EQDhr9Z7Ymny5K3EHmIxHUsrXPEnu9axOKTG"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1