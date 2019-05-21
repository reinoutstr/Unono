#imports
import json
import time
import math

#load json file (read-write mode)
cards = json.load(open('cards.json', 'r+'))

#declare playstack
playStack = []

#declare player arrays
player1 = []
player2 = []
player3 = []
player4 = []
players = [player1, player2, player3, player4] #might not be needed, unsure
playerNames = []

#Game
print('Welcome to Uno: Endgame!')
input('Press enter to continue...')

