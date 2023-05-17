#!/usr/bin/env python3
from turtle import Turtle


class WriteState(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_answer(self, state, x, y):
        self.goto(x, y)
        self.write(state)
