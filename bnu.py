import random
rood0=[1, 0]
rood1=[1, 1]
rood2=[1, 2]
rood3=[1, 3]
rood4=[1, 4]
rood5=[1, 5]
rood6=[1, 6]
rood7=[1, 7]
rood8=[1, 8]
rood9=[1, 9]
rood10 = [1, 10] #pak twee kaarten

green0 = [2, 0]
green1 = [2, 1]
green2 = [2, 2]
green3 = [2, 3]
green4 = [2, 4]
green5 = [2, 5]
green6 = [2, 6]
green7 = [2, 7]
green8 = [2, 8]
green9 = [2, 9]
green10 = [2, 10]

blauw0 = [3, 0]
blauw1 = [3, 1]
blauw2 = [3, 2]
blauw3 = [3, 3]
blauw4 = [3, 4]
blauw5 = [3, 5]
blauw6 = [3, 6]
blauw7 = [3, 7]
blauw8 = [3, 8]
blauw9 = [3, 9]
blauw10 = [3, 10]

yellow0 = [4, 0]
yellow1 = [4, 1]
yellow2 = [4, 2]
yellow3 = [4, 3]
yellow4 = [4, 4]
yellow5 = [4, 5]
yellow6 = [4, 6]
yellow7 = [4, 7]
yellow8 = [4, 8]
yellow9 = [4, 9]
yellow10 = [4, 10]

wild1 = [5, 0]
wild2 = [5, 1]

allcards=[wild1, wild2, rood0, rood1, rood2, rood3, rood4, rood5, rood6, rood7, rood8, rood9, rood10, green0, green1, green2, green3, green4, green5, green6, green7, green8, green9, green10, blauw0, blauw1, blauw2, blauw3, blauw4, blauw5, blauw6, blauw7, blauw8, blauw9, blauw10, yellow0, yellow1, yellow2, yellow3, yellow4, yellow5, yellow6, yellow7, yellow8, yellow9, yellow10]
tempcards=[wild1, wild2, rood0, rood1, rood2, rood3, rood4, rood5, rood6, rood7, rood8, rood9, rood10, green0, green1, green2, green3, green4, green5, green6, green7, green8, green9, green10, blauw0, blauw1, blauw2, blauw3, blauw4, blauw5, blauw6, blauw7, blauw8, blauw9, blauw10, yellow0, yellow1, yellow2, yellow3, yellow4, yellow5, yellow6, yellow7, yellow8, yellow9, yellow10]

player1=[]
player2=[]
player3=[]
player4=[]

players = [player1, player2, player3, player4]
#kaarten uitdelen

for x in range(len(players)):
  for y in range(5):
    currentplayerarray = players[x]
    plo = random.randint(1, len(tempcards))
    currentplayerarray.append(allcards[plo])
    tempcards.pop(plo)
  # print(players[x])

# start spel


def choosingcard(firstcard):
  for x in players:
    nummer = 0

    topcard = allcards[firstcard]
    if topcard == wild1: #If there's a wild card these actions are taken
      for y in range(2):
        currentplayerarray = x
        plo = random.randint(0, len(tempcards))
        currentplayerarray.append(allcards[plo])
        tempcards.pop(plo)
      print('You got 2 cards...')
    elif topcard == wild2:
      for y in range(4):
        currentplayerarray = x
        plo = random.randint(0, len(tempcards))
        currentplayerarray.append(allcards[plo])
        tempcards.pop(plo)
      print('You got 4 cards...')

    #print("It's now ", x, ' turn')
    print ('The card on top is: ', topcard)
    print ('Your cards: ', x)
    
    nummer=int(input('Choose a card: '))
    
    if nummer > (len(x)-1):
      print('This number is too high')
      print('Skipping to next player...')
      choosingcard(firstcard)
      
    if nummer == -1:
      print('bitch')
      addplayer = x
      add = random.randint(0, len(tempcards))
      addplayer.append(tempcards[add])
      tempcards.pop(add)
      print('.')
      choosingcard(firstcard)
    
    chosencard = x[nummer]
    
    kleurkaart=chosencard[0]
    nummerkaart=chosencard[1]
    
    print (chosencard)
    
    kleurcheck = topcard[0]
    nummercheck = topcard[1]
    
    if kleurcheck == kleurkaart and chosencard in x:
      print('You can place this card on the stack!')
      if input('Are you sure you want to place this card? ') == "yes":
       #verwijder het kaart uit het players hand en voeg hem toe aan de stapel
       x.remove(chosencard)
       firstcard = chosencard
       firstcard = allcards.index(firstcard)
       print('.')
      
      else:
         print('which card else do you wanna lay down')
         print('.')

      
    elif nummercheck == nummerkaart:
      
      print('card available, would you like to put it down?')
      
      if input() == "yes":
       #verwijder het kaart uit het players hand en voeg hem toe aan de stapel
       firstcard = chosencard
       firstcard = allcards.index(firstcard)
       print('.')
        
      else:
        print('which card else do you wanna lay down')
        print('.')

      
    else:
      
      print('please try again')
      print('.')
      #choosingcard(firstcard)
    #print(topcard)
  choosingcard(firstcard)





p = random.randint(1,len(allcards))
print(p)
choosingcard(p)
