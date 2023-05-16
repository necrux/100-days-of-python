#!/usr/bin/env python3
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
SCORE_FILE = 'data.txt'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(SCORE_FILE, 'r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.set_score()
        self.hideturtle()

    def set_score(self):
        self.goto(0, 265)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.set_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SCORE_FILE, 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.set_score()
