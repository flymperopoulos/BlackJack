import random

def createDeck(numberOfDecks):
	# Create an empty newDeck
	newDeck = []

	# Define a list of suits and a dictionary of card values
	cardTypes = ['Clubs','Spades','Diamonds','Hearts']
	cardNumbers = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7,'8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}

	# Number of piles initialized
	numberofPiles = 0

	# Append cardTypes and cardNumbers accordingly
	while numberofPiles < numberOfDecks:
		for suit in cardTypes:
			newL = []
			for key in cardNumbers:
				newL.append([suit,[key,cardNumbers[key]]])
			newDeck.append(newL)
		numberofPiles += 1

	# Determines the number of decks used
	# print "The amount of decks used equals " + str(len(newDeck)/4) + "."

	# Return the final Deck	
	return newDeck

# print createDeck(1)

def see_choices(decks, currentScore, nextDecision, whoPlays):

	# nextDecision = str(raw_input("Do you want to hit or pass? "))
	# whoPlays = str(raw_input("Do you want to be the player or the dealer? "))
	# Examines the player's case
	if whoPlays == 'player':
		if nextDecision == 'pass':
			print "Your current score is still equal to " + str(currentScore) + "."
			return currentScore
		if nextDecision == 'hit':
			newCard = random.choice(random.choice(createDeck(1)))
			# print newCard
			typeNewCard = "You drew a " + newCard[1][0] + " of " + newCard[0] + "."
			# print typeNewCard
			newScore = currentScore + newCard[1][1]
			print "Your new score is " + str(newScore)
			return newScore

	# Examines the dealer's case
	if whoPlays == 'dealer':
		if nextDecision == 'pass':
			print "The dealer stands and his remaining total is " + str(currentScore)
			return currentScore
		if nextDecision == 'hit':
			newCardDealer = random.choice(random.choice(createDeck(1)))
			newScoreDealer = currentScore + newCardDealer[1][1]
			print "The dealers new score is " + str(newScoreDealer)
			return newScoreDealer

# print see_choices(createDeck(1),10, 'hit', 'player')

def see_more_choices(decks, whoPlays, currentScore):

	if whoPlays == 'player':

		# Asks the player to input next decision
		nextDecision = str(raw_input("What is going to be your next step, hit or pass? "))
		currentScore = see_choices(decks, currentScore, nextDecision, whoPlays)
		return currentScore

	if whoPlays == 'dealer':

		# Pre-determines the dealer's decision making proces.
		if currentScore >= 16:
			nextDecision = 'pass'
		if currentScore <= 15:
			nextDecision = 'hit'
		currentScore = see_choices(decks, currentScore, nextDecision, whoPlays)
		return currentScore

def alternating(candidateTurn, dealerTurn):

	playerTotal = candidateTurn[0]
	playerChoice = candidateTurn[1]
	dealerTotal = dealerTurn[0]
	dealerChoice = dealerChoice[1]

	endingMessage = '\n' + 'The game is over.' + '\n' + 'Your score is: ' + str(playerTotal) + '\n' + 'The dealer has a score of ' + str(dealerTotal) + '\n' + 'See you soon!'
	
	if playerChoice == 'pass':
		if playerTotal == 21 and dealerTotal < 21:
			print endingMessage
			print "You won!"
			return
		if playerTotal < 21 and dealerTotal == 21:
			print endingMessage
			print "The dealer got a 21. You lost..."
			return
		if playerTotal < 21 and dealerTotal > 21:
			print endingMessage
			print "The dealer got bust. You win!"
			return
		if playerTotal == dealerTotal:
			print "Nobody won. You got the same score."
			return
		if dealerChoice == 'pass':
			if playerTotal < dealerTotal:
				print endingMessage
				print 'The house wins.'
				return
			elif dealerTotal < playerTotal:
				print endingMessage
				print 'You won the house!'
				return

	if playerChoice == 'hit':
		if playerTotal == 21 and dealerTotal < 21:
			print endingMessage
			print "You won."
			return
		if playerTotal == 21 and dealerTotal == 21:
			print endingMessage
			print "Both the dealer and you win."
			return
		if playerTotal < 21 and dealerTotal == 21:
			print endingMessage
			print "Dealer got a 21 first. You lost."
			return	
		if dealerTotal > 21:
			print "The dealer exceeded the 21 limit. You win!"
			return
		if playerTotal > 21:
			print "You exceeded the 21 limit. You lose..."	

def mainOne():
	newDeck = createDeck(1)

	toStart = str(raw_input('Hello, you are ready to start playing BlackJack. Please type "go" if you want to proceed: '))

	while toStart != 'go':
		toStart = str(raw_input("Remember, only if you type 'go', will you proceed to play the game. "))

	if toStart == 'go':

		# using the same pattern as before
		cardNo1Player = random.choice(random.choice(newDeck))
		characterCardNo1Player = str(cardNo1Player[1][0]) + ' of ' + cardNo1Player[0]

		print "First card is " + characterCardNo1Player

		cardNo2Player = random.choice(random.choice(newDeck))
		characterCardNo2Player = str(cardNo2Player[1][0]) + ' of ' + cardNo2Player[0]

		cardNo3Player = random.choice(random.choice(newDeck))
		characterCardNo3Player = str(cardNo3Player[1][0]) + ' of ' + cardNo3Player[0]

		print "The second card turns out to be " + characterCardNo2Player

		print "The third card turns out to be " + characterCardNo3Player

		print "Hence, the current total value of your hand is " + str(cardNo1Player[1][1] + cardNo2Player[1][1] + cardNo3Player[1][1]) 

		print "Let's now see what the dealer has. We can only see one of the two cards he possesses."

		cardNo1Dealer = random.choice(random.choice(newDeck))
		characterCardNo1Dealer = str(cardNo1Dealer[1][0]) + ' of ' + cardNo1Dealer[0]

		cardNo2Dealer = random.choice(random.choice(newDeck))
		characterCardNo2Dealer = str(cardNo2Dealer[1][0]) + ' of ' + cardNo2Dealer[0]

		cardNo3Dealer = random.choice(random.choice(newDeck))
		characterCardNo3Dealer = str(cardNo3Dealer[1][0]) + ' of ' + cardNo3Dealer[0]

		print " The Dealer's open card is: " + characterCardNo1Dealer

		dealerCurentTotal = cardNo1Dealer[1][1] + cardNo2Dealer[1][1] + cardNo3Dealer[1][1]
		
		candidateTurn = see_more_choices(newDeck, 'player', (cardNo1Player[1][1] + cardNo2Player[1][1] + cardNo3Player[1][1]))
		dealerTurn = see_more_choices(newDeck, 'dealer', dealerCurentTotal)

if __name__ == '__main__':
	mainOne()