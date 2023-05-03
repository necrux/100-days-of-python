#!/usr/bin/env python3
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
import random
from art import logo

def get_card(opponent, count):
    """Return X random cards from the deck where X = count."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for card in range(0, count):
        opponent.append(random.choice(cards))
    return opponent

def check_ace(opponent):
    """Reduce the value of the ace if it were to cause a bust."""
    if sum(opponent) > 21 and 11 in opponent:
        opponent.remove(11)
        opponent.append(1)
    return opponent

def main():
    play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    while play == "y": 
        os.system("clear")
        print(logo)
        player_blackjack = False
        dealer_blackjack = False
        player = []
        dealer = []
        player = get_card(player, 2)
        dealer = get_card(dealer, 2)
        print(f"\tYour cards: {player}, current score: {sum(player)}")
        print(f"\tComputer's first card: {dealer[0]}")
        if sum(player) == 21:
           player_blackjack = True
        if sum(dealer) == 21: 
            dealer_blackjack = True
        hit = "y"
        while hit == "y":
            if sum(player) == 21:
                break
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                player = get_card(player, 1)
                print(f"\tYou drew a {player[-1]}, current score: {sum(player)}")
            if sum(player) >= 21:
                break
        # Force draw for dealer if under 17.
        while sum(dealer) <= 16:
            dealer = get_card(dealer, 1)
        dealer = check_ace(dealer)
        player = check_ace(player)
        print(f"\tYour final hand: {player}, final score: {sum(player)}")
        print(f"\tComputer's final hand: {dealer}, final score: {sum(dealer)}")

        if sum(player) > 21:
            print("You went over. You lose :(")
        elif sum(player) == sum(dealer):
            print("Draw.")
        elif player_blackjack:
            print("Blackjack! You win!")
        elif sum(player) > sum(dealer):
            print("You win!")
        elif dealer_blackjack:
            print("You lose. Dealer wins with a Blackjack.")
        elif sum(dealer) <= 21 and sum(dealer) > sum(player):
            print("Dealer wins.")
        else:
            print("Dealer busts. You win!")

        play = input(f"Do you want to play another hand? Type 'y' or 'n': ")

if __name__ == "__main__":
    os.system("clear")
    main()
