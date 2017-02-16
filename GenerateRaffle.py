from twython import Twython

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

raffle = {}

followers = t.get_followers_ids(screen_name = "DomEnterprises", stringify_ids=true)['ids']
# adds each user with hashtage #hacku5 to raffle list
for tweet in tweets:
	raffle[tweet['id_str']] = tweet['user']['screen_name']

# users that tweeted the hashtag but are not following @DomEnterprises
waitingList = {}

# get followers of @DomEnterprises 


# for each user in the raffle but not following @DomEnterprises add them to waiting list
for userID in raffle:
	if userID not in followers:
		waitingList[userID] = raffle[userID]
		#generateResponseTweet("Follow DomEnterprises on Twitter to get a Raffle Ticket")

# delete all the raffle participants that were added to the waiting list
#for key in waitingList:
#	del raffle[key]


print raffle


