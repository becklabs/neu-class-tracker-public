import json
import tweepy
from termcolor import colored


class Tweeter:
    def __init__(self):
        with open("twitter_creds.json") as f:
            twitter_creds = json.load(f)
        twitter_creds = dict(twitter_creds)
        API_KEY = twitter_creds['API_KEY']
        API_SECRET = twitter_creds['API_SECRET']
        ACCESS_TOKEN = twitter_creds['ACCESS_TOKEN']
        ACCESS_SECRET = twitter_creds['ACCESS_SECRET']

        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        self.api = tweepy.API(auth)

    def save(self, message):
        with open('temp.txt', 'w') as f:
            f.write(message)

    def tweet(self, tweet):
        self.save(tweet)
        try:
            with open('temp.txt', 'r') as f:
                self.api.update_status(f.read())
        except tweepy.TweepError as e:
            print(e)
