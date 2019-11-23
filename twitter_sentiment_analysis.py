import tweepy
import twitter_cred
from textblob import TextBlob
import openpyxl
from openpyxl import load_workbook
import preprocessor as p
import re
import nltk


def auth_twitter():
    """
    Function for authenticating twitter account
    :return:
    """
    auth = tweepy.OAuthHandler(twitter_cred.CON_API_KEY, twitter_cred.CON_API_KEY_SECRET)
    auth.set_access_token(twitter_cred.ACCESS_TOKEN, twitter_cred.ACCESS_TOKEN_SECRET)
    return auth


def get_api(auth):
    """
    Fuction that returns the twitter api
    :param auth:
    :return:
    """
    api = tweepy.API(auth)
    return api


def get_public_tweets(api, search_query):
    """
    Fuction returns the public tweets
    :param api:
    :param search_query:
    :return:
    """
    # public_tweets = api.search(search_query, count=1000, lang='en')

    public_tweets = tweepy.Cursor(api.search, q=search_query, lang='en').items(1000)
    return public_tweets


def display_tweets(public_tweets):
    """
    Fuction displays the first 100 tweets
    :param public_tweets:
    :return:
    """
    count = 1
    for tweet in public_tweets:
        if count < 100:
            print(tweet.text)
            analysis = TextBlob(tweet.text)
            print(analysis.sentiment)
        else:
            break

        count = count + 1


def get_data(tweets):
    """
    Function returns the tweet, its polarity and its subjectivity

    :param tweets:
    :return:
    """
    jnu_tweets = []
    tweets_polarity = []
    tweets_subjectivity = []

    count = 1

    for tweet in tweets:
    	t = p.clean(tweet.text)

    	# removing colons from the tweet
    	t = re.sub(r':', '', t)

    	# removing mentions
    	t = re.sub(r'‚Ä¶', '', t)

    	# removing non ascii characters
    	t = re.sub(r'[^\x00-\x7F]+',' ', t)

    	jnu_tweets.append(t)
    	tweets_polarity.append(TextBlob(t).polarity)
    	tweets_subjectivity.append(TextBlob(t).subjectivity)
        

    return jnu_tweets, tweets_polarity, tweets_subjectivity


def create_file(file_name, public_tweets):
    """
    This function simply creates a excel file having three columns of tweet, polarity and subjectivity

    :param file_name:
    :param public_tweets:
    :return:
    """
    tweets, polarity, subjectivity = get_data(public_tweets)
    wb = openpyxl.Workbook()
    sheet = wb.active

    c = sheet.cell(1, 1)
    c.value = "Tweets"

    c = sheet.cell(1, 2)
    c.value = "Polarity"

    c = sheet.cell(1, 3)
    c.value = "Subjectivity"

    row = 2
    for t in tweets:
        c = sheet.cell(row, 1)
        c.value = t
        row = row + 1

    row = 2
    for p in polarity:
        c = sheet.cell(row, 2)
        c.value = p
        row = row + 1

    row = 2
    for s in subjectivity:
        c = sheet.cell(row, 3)
        c.value = s
        row = row + 1

    wb.save(file_name)
    print("File created successfully")


if __name__ == '__main__':
    twitter_auth = auth_twitter()
    twitter_api = get_api(twitter_auth)
    twitter_tweets = get_public_tweets(twitter_api, '#standwithjnu')

    # print(len(twitter_tweets))

    # Displaying first 100 tweets
    # display_tweets(twitter_tweets)

    create_file("tweets.xlsx", twitter_tweets)
