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

def see_choices(decks, whoPlays, currentScore,nextDecision):

	# nextDecision = raw_input("Do you want to hit or pass? ")
	# Examines the player's case
	if whoPlays == 'player':
		if nextDecision == 'pass':
			return "Your current score is still equal to " + str(currentScore) + "."
		if nextDecision == 'hit':
			newCard = random.choice(random.choice(createDeck(1)))
			print newCard
			typeNewCard = "You drew a " + newCard[1][0] + " of " + newCard[0] + "."
			print typeNewCard
			newScore = currentScore + newCard[1][1]
			return "Your new score is " + str(newScore)

print see_choices(createDeck(1),'player',10,'hit')
			


