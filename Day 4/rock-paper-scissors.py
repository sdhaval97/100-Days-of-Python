# Creating the famous Rock, Paper, Scissors Game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Asking the user for their choice

game_patterns = [rock, paper, scissors]
user = int(input("What do you choose:\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n"))
print("You chose:\n")
print(game_patterns[user])

computer = random.randint(0,2)
print("The computer chose:\n")
print(game_patterns[computer])

# Setting the condition for victory

if user == computer:
    print("The Round is draw!")

elif user == 0:
    if computer == 1:
        print("Computer wins this round!")
    else:
        print("You win this round!")

elif user == 1:
    if computer == 0:
        print("You win the round!")
    else:
        print("The computer wins this round!")

elif user == 2:
    if computer == 0:
        print("The computer wins this round!")
    else:
        print("You win this round!")

print("Thank you for playing!")

