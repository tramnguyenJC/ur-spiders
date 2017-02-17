from django.shortcuts import render
from twython import Twython
from Raffle import Raffle
from django.http import JsonResponse

# Create your views here.
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

# adds each user with hashtage #hacku5 to raffle list
for tweet in tweets:
	raffle[tweet['id_str']] = tweet['user']['screen_name']

lottery = Raffle(raffle)

def tickets_choose(request):
    winner = lottery.generateRaffle()
    return JsonResponse({'winner':winner})

def tickets_list(request):
	return render(request, 'tickets/tickets_list.html', {"raffle":raffle.values()})
