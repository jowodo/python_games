#!/usr/bin/python3
# inspired by manu m

import random
randomnumber = random.randint(0,2)
print("Enter: schere, stein or papier")
hand = str(input()).lower()
#hand = "schere"

choices=["schere","stein","papier"]
robohand =choices[randomnumber]

def fight(robo,player):
    if (choices.index(robo)+1)%3 == choices.index(player)%3:
        print ("you win with "+player+" against "+ robo)
    elif robo == hand:
        print ("you both chose "+ robo)
    else:
        print("you lose with "+ player+ " against ", robo)

if hand in choices:
    fight(robohand,hand)
else:
    print("please chose from 'schere','stein' or 'papier'")
