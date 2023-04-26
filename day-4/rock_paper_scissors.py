#!/usr/bin/env python3
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

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

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]

print("Classic Rock, Paper, Scissors Game")

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
player1 = int(input())
player2 = random.randint(0,2)

if player1 == 0:
    print(rock)
elif player1 == 1:
    print(paper)
elif player1 == 2:
    print(scissors)
else:
    print("You must enter a valid number.")
    exit(1)

print("Computer chose:")
print(game_images[player2])

if (player1 == 0 and player2 == 2) or (player1 == 1 and player2 == 0) or (player1 == 2 and player2 == 1):
    print("You win.") 
elif player1 == player2:
    print("Tie.")
else:
    print("You lose.")
