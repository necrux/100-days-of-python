#!/usr/bin/env python3
from turtle import Turtle

FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level()

    def level(self):
        self.clear()
        self.goto(-280, 265)
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def increment_level(self):
        self.current_level += 1
        self.level()

    def game_over(self):
        self.goto(-35, 0)
        self.write("Game Over", align="left", font=("Courier", 15, "bold"))
