#!/usr/bin/env python3
# Maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Not a fan of this solution and it can take many steps to complete.
# I need to do better at describing the problem; in this case it never had a wall on it's right;
# I _should_ have had an initial loop to get the robot to a wall then proceed with the main logic.

def turn_right():
    for i in range(3):
        turn_left()

def break_loop():
    while not wall_on_right() and not wall_in_front():
        move()
        
count = 0

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    else:
        turn_left()
    count += 1
    if count == 10:
        break_loop()
        count = 0
