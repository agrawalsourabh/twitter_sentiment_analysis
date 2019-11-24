import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import twitter_cred

auth = OAuthHandler(twitter_cred.CON_API_KEY, twitter_cred.CON_API_KEY_SECRET)
auth.set_access_token(twitter_cred.ACCESS_TOKEN, twitter_cred.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


class MyListener(StreamListener):
    def on_data(self, raw_data):
        try:
            with open("jnu.json", 'a') as f:
                f.write(raw_data)
                return True
        except BaseException as e:
            print("Error: " + str(e))
        return True

    def on_error(self, status_code):
        print(status_code)
        return True


print(len(api.search(['jnuprotest', 'jnu'], count=100)))
# twitter_stream = Stream(auth, MyListener())
# twitter_stream.filter(track=['jnuprotest', 'jnu'])
