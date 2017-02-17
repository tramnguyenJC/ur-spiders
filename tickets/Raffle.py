import random
from models import RaffleWinner


class Raffle:

	def __init__(self, users):
		self.tweeters = users

	def hasWonBefore(self, tweetID):
		for raffleWinner in RaffleWinner.objects.all():
			if raffleWinner.tweet_id == tweetID:
				return True

		return False

	def generateRaffle(self):

		# get list of tweet ids
		userIDs = list(self.tweeters)

		# pick a winner id at random
		winnerID = random.choice(userIDs)

		# keep picking a winner id at random until you get a person that hasn't won
		while self.hasWonBefore(winnerID):
			winnerID = random.choice(userIDs)

		# get the name associated with the winner id
		winnerName = self.tweeters[winnerID]

		# remove the raffle winner from the list of contestants
		del self.tweeters[winnerID]

		# save a reference to the
		p = RaffleWinner(tweet_id=winnerID)
		p.save()

		return winnerName