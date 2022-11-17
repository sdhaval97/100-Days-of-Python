# Creating a treasure island game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Asking the user where they want to turn

turn = input("Where do you want to turn: Left or right? ")

# Creating a condition for the first stage

if turn == 'left':
    swim = input("Do you want to swim or wait? ")

    # Creating a condition for the second stage
    
    if swim == 'wait':
        door = input("Which door do you select: Red, Blue, or Yellow? ")

        # Creating a condition for the third stage

        if door == 'red':
            print("Burned by Fire.\nGame over.")
        elif door == 'blue':
            print("Eaten by beasts.\nGame over.")
        elif door == 'yellow':
            print("You win!")
        else:
            print("Game over.")
    
    else:
        print("Attacked by trout.\nGame over.")
    
else:
    print("Fall into a hole.\nGame over.")