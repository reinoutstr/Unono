#imports
import json
import time
import math

#load json file (read-write mode)
cards = json.load(open('cards.json', 'r+'))

#declare playstack
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

cardtype = random.choice([blue,red,yellow,green,special])
carchoice = random.choice(cardtype)
if cardchoice not in special or cardchoice.split("#")[1] not in ["skip", "flip", "two+"]:
	playStack.append(cardchoice)
# microsoft diagnostics tool irl
time.sleep(3)
print("Done dealing!")
time.sleep(1)
print("Let's start!")
time.sleep(1)
