import csv
from Tweet import make_tweet
import glob
import os
from sklearn.externals import joblib

class Database_manager(object):

    db=None
    cur=None

    def __init__(self):
        """
         If you want to recover tweets from a mysql db set the config.py:
         for example  mysql = {
         'host': 'yourhost',
         'user': 'yourmysqluser',
         'passwd': 'yourpassword',
         'db': 'dbname'}
        """



    def return_tweets(self):
        """Return an array containing tweets.
           Tweets are encoded as Tweet objects.
        """
        """
         You could recover tweets from db or csv file

        """
        tweets=self.return_tweets_training()+self.return_tweets_test()

        print(len(tweets))
        return tweets

    def return_tweets_training(self):
        """Return an array containing tweets.
           Tweets are encoded as Tweet objects.
        """
        """
         You could recover tweets from db or csv file

        """

        if os.path.isfile('tweets_train.pkl') :
            tweets= joblib.load('tweets_train.pkl')
            return tweets

        tweets=[]

        filelist = sorted(glob.glob("data/IroSvA-training/*.csv"))


        for file in filelist:
            first = True

            csvfile=open(file, newline='')
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for tweet in spamreader:

                if not first: #

                        id=tweet[0]
                        text=tweet[3]
                        language=file.split(".")[1]
                        topic=tweet[1]
                        label=tweet[2]

                        """
                        Create a new istance of a Tweet object
                        """
                        this_tweet=make_tweet(id, text, label,language,topic)

                        tweets.append(this_tweet)

                first = False

        joblib.dump(tweets, 'tweets_train.pkl')

        return tweets


    def return_tweets_test(self):
        """Return an array containing tweets.
           Tweets are encoded as Tweet objects.
        """
        """
         You could recover tweets from db or csv file

        """
        if os.path.isfile('tweets_test.pkl') :
            tweets= joblib.load('tweets_test.pkl')
            return tweets

        tweets=[]

        filelist = sorted(glob.glob("data/IroSvA-test/*.csv"))

        for file in filelist:
            first = True

            csvfile=open(file, newline='')
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for tweet in spamreader:
                if not first:
                    id=tweet[0]
                    text=tweet[3]
                    language=file.split(".")[1]
                    topic=tweet[1]
                    label=tweet[2]

                    """
                    Create a new istance of a Tweet object
                    """
                    this_tweet=make_tweet(id, text, label,language,topic)

                    tweets.append(this_tweet)

                first=False

        joblib.dump(tweets, 'tweets_test.pkl')

        return tweets




def make_database_manager():
    database_manager = Database_manager()

    return database_manager




if __name__== "__main__":
    database_manager = Database_manager()

    tweets=database_manager.return_tweets_training()
    print("Tweets train")
    for tweet in tweets:
        print(tweet.id,tweet.text,tweet.language,tweet.label,tweet.topic)
    tweets=database_manager.return_tweets_test()
    print("Tweets test")
    for tweet in tweets:
        print(tweet.id, tweet.text, tweet.language, tweet.label, tweet.topic)

    tweets = database_manager.return_tweets()
    print("Tweets")
    for tweet in tweets:
        print(tweet.id, tweet.text, tweet.language, tweet.label, tweet.topic)
