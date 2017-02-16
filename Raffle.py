import random

class Raffle:

	def __init__(self, tweeters):
		self.tweeters = tweeters

	def generateRaffle(self):

		userIDs = self.tweeters.keys()
		winnerID = random.choice(userIDs)

		winnerName = self.tweeters[winnerID]

		del self.tweeters[winnerID]

		return winnerName