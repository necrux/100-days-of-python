#!/usr/bin/env python3

import random
from turtle import Turtle

COLORS = ["blue", "red", "yellow", "green", "purple"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        color = random.choice(COLORS)
        self.color(color)
        self.goto(random_x, random_y)
