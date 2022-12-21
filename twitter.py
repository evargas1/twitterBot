from http import client
import tweepy
import time
import os

bearer_token = os.getenv('BEARER_TOKEN')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
  
# client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)


query = '#TheKardashians from:25365536 lang:en -is:retweet'
# tweet_fields=['context_annotations', 'created_at'],
query2 = '(happy OR happiness) lang:en -birthday -is:retweet'


screen_name = ''
screen_id = client.get_user(username=screen_name)
print(screen_id)

def retireve_tweet_id(tweets_info):
    for tweet in tweets_info.data:
        return tweet.id


def check_mentions(query, since_id):
    new_since_id = since_id
    tweets = client.search_recent_tweets(query=query,  max_results=10)
    if tweets.data == None:
        return new_since_id
    else:
        for tweet in tweets.data:
            new_since_id = max(tweet.id, new_since_id)
            tweet_id = tweet.id
            retweet_now = client.retweet(tweet_id)
            print(retweet_now)

        return new_since_id

def main():
    since_id = 1
    while True:
        since_id = check_mentions('#working from: lang:en -is:retweet', since_id)
        print(since_id)
        time.sleep(5)

if __name__ == "__main__":
    main()

