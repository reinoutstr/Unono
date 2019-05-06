def evalCard(card, playerlist, playstack):
    if not card in playerlist:
        return 1
    else:
        if card == "wild" or "wild+":
            return 0
        else:
            lastCardIndex = len(playstack) - 1
            lastCard = playstack[lastCardIndex]
            