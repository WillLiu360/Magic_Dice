import dice
import random

print("Pick up your dice and fight!")

d6=dice.Dice("D6",
             list(range(1,7)),
             #[1,2,3,4,5,6,],
             )
#print(d6.sides)

inv=[d6.name]

print("Dices in your pocket: "
      +inv[0]
      +"""
       Which dice would you like to roll?"""
      )

def roll_dice():
    output=random.choice(d6.sides)
    print("You rolled: "+str(output))

roll_dice()
