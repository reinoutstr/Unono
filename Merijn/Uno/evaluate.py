def evalCard(userchoice, player, playStack):
	currentCard = playStack[-1] #Get the last card from the stack	
	if userchoice in blue && currentCard in blue: #Check if the colors of the cards are compatibel
		return true
	elif userchoice in red && currentCard in red:
		return true
	elif userchoice in green && currentCard in green:
		return true
	elif userchoice in yellow && currentCard in yellow:
		return true
	elif userchoice in special:
		return true
	else:
		currentCardNumberArray = currentCard.split("#") #Splits the card data in two
		currentCardNumber = currentCardNumberArray[1] #Sets a new variable with only the number of the card
	
		userchoiceArray = currentCard.split("#") #Splits the card data in two
		userchoiceNumber = userchoiceArray[1] #Sets a new variable with only the number of the card
	
		if userchoiceNumber == currentCardNumber: #Checks if the number of the two cards the same are
			return true
		else: 
			return false