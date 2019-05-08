# imports
import json
import math
import random
import checkdecks
import cardevaluate
import time
# load JSON files (read mode)
cards = json.load(open('cards.json','r'))

# declare card color sets
blue = cards["blue"]
red = cards["red"]
yellow = cards["yellow"]
green = cards["green"]
special = cards["special"]

# declare playstack
playStack = []

# declare player arrays
player1 = []
player2 = []
player3 = []
player4 = []
players = [player1, player2, player3, player4]
playersName = []

print("Welcome to Uno!")
input("Press any key to continue...")

playersName.append(input("Enter player 1's name: "))
playersName.append(input("Enter player 2's name: "))
playersName.append(input("Enter player 3's name: "))
playersName.append(input("Enter player 4's name: "))
print(playersName)

print("Handing cards out...")


for x in range(4):
    current_deal_player = players[x]
    successful = 0
    while not successful:
        cardtype = random.choice([blue, red, yellow, green, special])
        cardchoice = random.choice(cardtype)
        # if cardchoice not in player1 and cardchoice not in player2 and cardchoice not in player3 and cardchoice not in player4:
        if not checkdecks.checkdecks(cardchoice, player1, player2, player3, player4):
            current_deal_player.append(cardchoice)
        if len(current_deal_player) == 7:
            successful = 1


# microsoft diagnostics tool irl
time.sleep(3)
print("Done dealing!")
time.sleep(1)
print("Let's start!")
time.sleep(1)

round = "cw"

while round == "cw":
    i = 0
    for x in players:
        print("It's now ", playersName[i], "'s turn.")
        print("Amount of cards: ", len(x))
        # print("\n\n Card on stack: ", playStack[len(playStack)-1])
        print("\n\nThese are your cards: ", x, sep='\n')
        userchoice = input('Type the card you want to play: ')
        evalResult = cardevaluate.evalCard(userchoice, x, playStack)
        if evalResult == 0:
            playStack.append(userchoice)
            x.remove(userchoice)
        i += 1

while round == "ccw":
    i = 3
    for x in reversed(players):
        print("It's now ", playersName[i], "'s turn.")
        print("Amount of cards: ", len(x))
        # print("\n\n Card on stack: ", playStack[len(playStack)-1])
        print("\n\nThese are your cards: ", x, sep='\n')
        #userchoice = input('Type the card you want to play: ')
        #    playStack.append(userchoice)
        #    x.remove(userchoice)
        i -= 1
