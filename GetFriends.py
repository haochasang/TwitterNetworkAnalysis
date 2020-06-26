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

def getUsers(filename):

    """
    extract a list of users from the json file we stored
    :param filename: the path of the json file
    :return: a set of user screen names
    """

    # loading the tweets from a json file
    tweets = json.load(open(filename))

    # initializing a list of user names
    users=[]

    # finding the users who tweet "DataScience"
    for tweet in tweets:
        # remove any tweets that do not have a retweet
        if tweet["retweet_count"]:
            users.append(tweet['user']['screen_name'])

    return set(users)


def save_friends_to_txt(user_name):

    with open('userList.txt', 'a+') as out:

        for user in api.friends(screen_name=user_name)["users"]:
            out.write(user_name+" "+user["screen_name"])
            out.write("\n")


if __name__ == "__main__":

    tweets_file = "tweets_DataScience.json"
    getUsers(tweets_file)
    users = getUsers(tweets_file)
    for user in users:
        save_friends_to_txt(user)
