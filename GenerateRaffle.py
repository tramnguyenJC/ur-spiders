from twython import Twython
import Contestant

TWITTER_APP_KEY = 'vgDa2r4tFyNyDsR0qSbFVNQev'
TWITTER_APP_KEY_SECRET = 'VzfMzSFYLCSM4NFPaMXRIgVrtEDtGPO1BhamDGZIlYW6ePuxJE'

TWITTER_ACCESS_TOKEN="832244289556140038-yZ5DltU262Dh4rsSEvdyHqnwLgDhu13"
TWITTER_ACCESS_TOKEN_SECRET="5hldQV6P5hPRIirMQajVrr7N446OrTqTznpJ6fyciPYUP"


t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#hacku5', count=100)

tweets = search['statuses']

raffle = []

# adds each user with hashtage #hacku5 to raffle list
for tweet in tweets:
	currentUser = Contestant(tweet['user']['screen_name'], tweet['id_str'])
	raffle.append(currentUser)

waitingList = []

for user in raffle:
	if !user.following('DomEnterprises'):
		waitingList.append(user)
		raffle.remove(user)
		generateResponseTweet("Follow DomEnterprises on Twitter to get a Raffle Ticket")
