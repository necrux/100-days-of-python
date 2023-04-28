#!/usr/bin/env python3
# Hurdle 4 challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    for i in range(3):
        turn_left()

def jump():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

# Solution 2 w/ wall_on_right
def turn_right():
    for i in range(3):
        turn_left()

def jump():
    if not front_is_clear():
        turn_left()
        while wall_on_right():
            move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
