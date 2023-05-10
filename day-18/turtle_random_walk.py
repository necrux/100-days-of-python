#!/usr/bin/env python3

import turtle
from random import choice, randint
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.width(25)
tim.speed(10)
turtle.colormode(255)

directions = [0, 90, 180, 270]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

while True:
    color = random_color()
    direction = choice(directions)
    tim.color(color)
    tim.left(direction)
    tim.forward(30)

screen = Screen()
screen.exitonclick()