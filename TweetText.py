import json
import csv

def getText(filename):
    """
    extract the text of a json file and save it to a csv file
    :param filename: the path of a json file that contains downloaded tweets
    """

    # loading the tweets from a json file
    tweets = json.load(open(filename))

    # writing the text to a csv file
    with open("TweetText.csv",'wb') as f:
        f.write('tweet\n'.encode('utf8'))
        for tweet in tweets:
            if tweet["text"]:
                f.write((tweet["text"]+"\n").encode('utf8'))


if __name__ == "__main__":

    getText("tweets_DataScience.json")
