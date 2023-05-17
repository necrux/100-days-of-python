#!/usr/bin/env python3
import turtle
import pandas
from write_states import WriteState

write_state = WriteState()

BG_IMAGE = "blank_states_img.gif"
STATES = "50_states.csv"

states = pandas.read_csv(STATES)
state_list = states.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(BG_IMAGE)
turtle.shape(BG_IMAGE)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        state_data = states[states.state == answer_state]
        write_state.write_answer(state=answer_state, x=int(state_data.x), y=int(state_data.y))
