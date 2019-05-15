# checks whether or not the max amount of cards of the type are in players' decks already, returns true when this is the case.
#"""random.choice(cardtype)"""

# function always returns 0 because it doesn't check two lists deep
def checkdecks(pcard, player1l, player2l, player3l, player4l):
    if pcard == "wild" or "wild+":
        if player1l.count(pcard) or player2l.count(pcard) or player3l.count(pcard) or player4l.count(pcard) == 4:
            return(1)
        else:
            return(0)
    if pcard == "r0":
        if player1l.count(pcard) or player2l.count(pcard) or player3l.count(pcard) or player4l.count(pcard) == 0:
            return(1)
        else:
            return(0)
    for x in range(1,10):
        if pcard == "b" + str(x) or "r" + str(x) or "y" + str(x) or "g" + str(x):
            if player1l.count(pcard) or player2l.count(pcard) or player3l.count(pcard) or player4l.count(pcard) == 2:
                return(1)
            else:
                return(0)
    for x in ["two+", "skip", "flip"]:
        if pcard == "b" + x or "r" + x or "y" + x or "g" + x:
            if player1l.count(pcard) or player2l.count(pcard) or player3l.count(pcard) or player4l.count(pcard) == 2:
                return(1)
            else:
                return(0)