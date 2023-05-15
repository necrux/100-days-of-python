#!/usr/bin/env python3
import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import CarManager

screen = Screen()

screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "w")

scoreboard = Scoreboard()
scoreboard.level()

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increment_level()
        car_manager.level_up()

screen.exitonclick()
