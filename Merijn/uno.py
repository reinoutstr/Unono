# imports
import json
import math
import random

# load JSON files (read mode)
cards = json.load(open('cards.json','r'))

# declare card color sets
blue = cards["blue"]
red = cards["red"]
yellow = cards["yellow"]
green = cards["green"]
special = cards["special"]

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
    print(x)
    current_deal_player = players[x]
    successful = 0
    while not successful:
        cardtype = random.choice([blue, red, yellow, green, special])
        cardchoice = random.choice(cardtype)
        print(cardchoice)
        if cardchoice not in player1 and cardchoice not in player2 and cardchoice not in player3 and cardchoice not in player4:
            current_deal_player.append(cardchoice)
        if len(current_deal_player) == 7:
            successful = 1
print(player1, player2, player3, player4, sep='\n')