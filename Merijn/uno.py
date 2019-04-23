# imports
import json
import math
import random

# load JSON files
cards = json.load(open('cards.json','r'))

# declare card color sets
blue = cards["blue"]
red = cards["red"]
yellow = cards["yellow"]
green = cards["green"]

print("Welcome to Uno!")
input("Press any key to continue...")

for 