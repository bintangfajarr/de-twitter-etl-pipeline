import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
from dotenv import load_dotenv
import os

def run_etl():
    load_dotenv()
    client = tweepy.Client(
        bearer_token=os.getenv("BEARER_TOKEN"),
        consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
        consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
        access_token=os.getenv("AWS_ACCESS_KEY"),
        access_token_secret=os.getenv("AWS_SECRET_KEY"),
        wait_on_rate_limit=True
    )
    user = client.get_user(username="ttomiokagiyuu")
    tweets = client.get_users_tweets(
        id=user.data.id,
        max_results=10,
        tweet_fields=["created_at", "public_metrics"],
        expansions=["author_id"],
        user_fields=["username"]
    )

    users = {u.id: u.username for u in tweets.includes["users"]}

    tweet_list = []

    for tweet in tweets.data:
        refined_tweet = {
            "user": users.get(tweet.author_id),
            "text": tweet.text,
            "favorite_count": tweet.public_metrics["like_count"],
            "retweet_count": tweet.public_metrics["retweet_count"],
            "created_at": tweet.created_at
        }
        tweet_list.append(refined_tweet)

    df=pd.DataFrame(tweet_list)
    df.to_csv("s3://x-etl-airflow-ec2/x_etl.csv")