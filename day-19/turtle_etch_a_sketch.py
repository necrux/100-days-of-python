#!/usr/bin/env python3

from time import sleep
from random import choice
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.speed(10)
tim.pensize(width=10)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tim.color(choice(colors))


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_drawing():
    tim.setx(0)
    tim.sety(0)
    tim.setheading(0)
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
