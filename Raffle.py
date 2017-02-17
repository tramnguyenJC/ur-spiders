import random

class Raffle:

	def __init__(self, users):
		self.tweeters = users

	def generateRaffle(self):

		userIDs = list(self.tweeters)
		winnerID = random.choice(userIDs)

		winnerName = self.tweeters[winnerID]

		del self.tweeters[winnerID]

		return winnerName