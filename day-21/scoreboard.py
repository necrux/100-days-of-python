#!/usr/bin/env python3
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.set_score()
        self.hideturtle()

    def set_score(self):
        self.goto(0, 265)
        self.clear()
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.set_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
