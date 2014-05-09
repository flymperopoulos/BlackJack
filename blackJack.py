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
	print "The amount of decks used equals " + str(len(newDeck)/4) + "."

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
			print newCard
			typeNewCard = "You drew a " + newCard[1][0] + " of " + newCard[0] + "."
			print typeNewCard
			print type(currentScore)
			print type(newCard[1][1])
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

if __name__ == '__main__':
	print see_more_choices(createDeck(numberOfDecks=1),'player',see_choices(createDeck(numberOfDecks=1),12,'hit','player'))
