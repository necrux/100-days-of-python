#!/usr/bin/env python3
import random
import tkinter
import pandas

BACKGROUND_COLOR = "#B1DDC6"
WORDS = "data/french_words.csv"
WORDS_TO_LEARN = "data/words_to_learn.csv"
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(WORDS_TO_LEARN, index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


# --------------------------- WORDS SETUP ------------------------------ #
try:
    data = pandas.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    data = pandas.read_csv(WORDS)
finally:
    to_learn = data.to_dict(orient="records")

# ---------------------------- UI SETUP ------------------------------- #
# Canvas
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "italic"))

# Buttons
yes_image = tkinter.PhotoImage(file="images/right.png")
yes_button = tkinter.Button(image=yes_image, command=is_known, highlightthickness=0)
yes_button.grid(column=2, row=2)

no_image = tkinter.PhotoImage(file="images/wrong.png")
no_button = tkinter.Button(image=no_image, command=next_card, highlightthickness=0)
no_button.grid(column=1, row=2)

next_card()

window.mainloop()
