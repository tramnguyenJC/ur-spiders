import tweepy

consumer_key = 'vgDa2r4tFyNyDsR0qSbFVNQev'
consumer_secret = 'VzfMzSFYLCSM4NFPaMXRIgVrtEDtGPO1BhamDGZIlYW6ePuxJE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token="832244289556140038-yZ5DltU262Dh4rsSEvdyHqnwLgDhu13"
access_token_secret="5hldQV6P5hPRIirMQajVrr7N446OrTqTznpJ6fyciPYUP"

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
#for tweet in public_tweets:
 #   print tweet.text


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'




raffleParticipants = dict()

for user in tweepy.Cursor(api.followers, screen_name="DomEnterprises").items():
    print user.screen_name
    #if (hasHackU()):
