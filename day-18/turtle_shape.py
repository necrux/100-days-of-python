#!/usr/bin/env python3

import turtle
from random import randint
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.width(10)
tim.speed(10)
turtle.colormode(255)

directions = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


count = 3
for _ in range(10):
    color = random_color()
    tim.color(color)
    turn = 360 / count
    for _ in range(count):
        tim.forward(100)
        tim.right(turn)
    count += 1

screen = Screen()
screen.exitonclick()
