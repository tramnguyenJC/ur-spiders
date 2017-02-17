import random
from winner.models import RaffleWinner


class Raffle:

	def __init__(self, users):
		self.tweeters = users

	def generateRaffle(self):
		ewrwernfdksm
		print >>sys.stderr, 'Goodbye, cruel world!'
		userIDs = list(self.tweeters)
		winnerID = random.choice(userIDs)

		winnerName = self.tweeters[winnerID]

		del self.tweeters[winnerID]

		# save a reference to the
		p = RaffleWinner(user_id=winnerID)
		p.save()

		print "before for loop"

		for a in RaffleWinner.objects.all():
			print "for loop"
			print a.user_id

		return winnerName