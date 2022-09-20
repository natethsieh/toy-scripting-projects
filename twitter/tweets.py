import tweepy
import os 
# apply for developer account
# set up way to store environment variables secretly 

consumer_key = os.environ['twitter_consumer_key']
consumer_secret = os.environ['twitter_consumer_secret']
access_token = os.environ['twitter_consumer_key']
access_token_secret = os.environ['twitter_access_token_secret']
# consumer_key = 'qelYRDNrbI7S3NUaPpl9uYhSM'
# consumer_secret = '4Say0Rlok485Pcj2PYNK9EN6iHctXPLSXXHqvyB03YrLqFi2Xj'
# access_token = '1074759289309282304-0TbQfNStFWqDJ8daM136OvPqAAoOEb'
# access_token_secret = 'wptijZIiyFlKyh0kZWzgHGWw1XMFLrEtY08oyZsxhgOcl'

auth = tweepy.OAuthHandler(
   consumer_key, consumer_secret
)
auth.set_access_token(
    access_token, access_token_secret
)

api = tweepy.API(auth)

user = api.me()
print(user.name)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)




def limit_handler(cursor):
    try:
        while True: 
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

## follow everyone back; or if follows > 100 
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()


## like tweets 
search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break