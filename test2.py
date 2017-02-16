from twython import Twython

TWITTER_APP_KEY = 'vgDa2r4tFyNyDsR0qSbFVNQev'
TWITTER_APP_KEY_SECRET = 'VzfMzSFYLCSM4NFPaMXRIgVrtEDtGPO1BhamDGZIlYW6ePuxJE'

TWITTER_ACCESS_TOKEN="832244289556140038-yZ5DltU262Dh4rsSEvdyHqnwLgDhu13"
TWITTER_ACCESS_TOKEN_SECRET="5hldQV6P5hPRIirMQajVrr7N446OrTqTznpJ6fyciPYUP"


t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#hacku5',   #**supply whatever query you want here**
                  count=100)

tweets = search['statuses']

for tweet in tweets:
  print tweet['user']['screen_name'], '\n', tweet['text'], '\n\n\n'