# Tweet deleter
# usage: run twitter_eraser.py with tweet.js in same directory
import twitter
import json

api = twitter.Api(
    # API key
    consumer_key='**********',
    # API secret
    consumer_secret='**********',
    # Access token
    access_token_key='**********',
    # Access secret
    access_token_secret='**********',
    sleep_on_rate_limit=True
)

with open('tweet.js', encoding='utf-8', mode='r') as f:
    tj=json.load(f)
    for tweet0 in tj:
        tweet = tweet0['tweet']
        print(tweet['id'])
        try:
            api.DestroyStatus(tweet['id'])
        except Exception as e:
            print(e.args)