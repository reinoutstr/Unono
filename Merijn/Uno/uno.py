# imports
import json
import math
import random
import checkdecks
# load JSON files (read mode)
cards = json.load(open('cards.json','r'))

# declare card color sets
blue = cards["blue"]
red = cards["red"]
yellow = cards["yellow"]
green = cards["green"]
special = cards["special"]

# array of action cards, don't mind too much
# actioncards = [two]

# declare player arrays
player1 = []
player2 = []
player3 = []
player4 = []
players = [player1, player2, player3, player4]

print("Welcome to Uno!")
input("Press any key to continue...")

print("Handing cards out...")


for x in range(4):
    current_deal_player = players[x]
    successful = 0
    while not successful:
        cardtype = random.choice([blue, red, yellow, green, special])
        print("Card type: ", cardtype)
        cardchoice = random.choice(cardtype)
        print("Card choice: ", cardchoice)
        # if cardchoice not in player1 and cardchoice not in player2 and cardchoice not in player3 and cardchoice not in player4:
        print(checkdecks.checkdecks(cardchoice, player1, player2, player3, player4))
        if not checkdecks.checkdecks(cardchoice, player1, player2, player3, player4):
            current_deal_player.append(cardchoice)
            print("Current player's deck: ", current_deal_player)
        if len(current_deal_player) == 7:
            successful = 1
print(player1, player2, player3, player4, sep='\n')

# # checks whether or not the max amount of cards of the type are in players' decks already, returns true when this is the case.
# def checkdecks(pcard, playersl):
#     if pcard == "wild" or "wild+":
#         if playersl.count(pcard) == 4:
#             return(1)
#         else:
#             return(0)
#     if pcard == "b0" or "r0" or "y0" or "g0":
#         if playersl.count(pcard) == 1:
#             return(1)
#         else:
#             return(0)
#     for x in range(1,10):
#         if pcard == "b" + str(x) or "r" + str(x) or "y" + str(x) or "g" + str(x):
#             if playersl.count(pcard) == 2:
#                 return(1)
#             else:
#                 return(0)
#     for x in ["two+", "skip", "flip"]:
#         if pcard == "b" + x or "r" + x or "y" + x or "g" + x:
#             if playersl.count(pcard) == 2:
#                 return(1)
#             else:
#                 return(0)