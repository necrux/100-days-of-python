#!/usr/bin/env python3
import os
from art import logo

def get_winner(auction):
    high_bid = 0
    for bidder in auction:
        price = auction[bidder]
        if price > high_bid:
            high_bid = price
            winner   = bidder 
    return winner, high_bid

print(logo)
print("Welcome to the secret auction program.")

bidders = "yes"
auction = {}

while bidders == "yes":
    name    = input("What is your name?: ")
    bid     = float(input("What is your bid?: $"))
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    auction[name] = bid

    os.system("clear")

    if bidders != "yes":
        winner, bid = get_winner(auction)
        print("The winner is {} with a bid of ${}.".format(winner, bid))
