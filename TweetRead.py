import tweepy
from tweepy import OAuthHandler
import Credentials as cd
import json
import time


# Credentials for Twitter API
consumer_key = cd.consumer_key
consumer_secret = cd.consumer_secret
access_token = cd.access_token
access_secret = cd.access_secret

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,
                 parser=tweepy.parsers.JSONParser(),
                 wait_on_rate_limit=True)

def getTweets(query):
    """
    create a json file and store the results of a specific query to the file
    :param query: twitter query
    :return: the path of the json file
    """

    # naming the file to store the downloaded tweets
    filename = 'tweets_'+query+".json"

    # using Search API to get relevant tweets that match the query and
    # saving the tweets to a json file
    tweets = api.search(q=query,lang='en',count=200)
    with open(filename,'w') as out:
        json.dump(tweets["statuses"], out, indent=4)

    return filename

if __name__ == "__main__":

    tweets_file = getTweets('DataScience')
