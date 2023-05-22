#!/usr/bin/env python3

import json
import tkinter
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip

JSON_VAULT = "data.json"

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def search():
    website = website_entry.get()
    try:
        with open(JSON_VAULT, "r") as data_file:
            data = json.load(data_file)
        email = data.get(website)["email"]
        password = data.get(website)["password"]
    except (TypeError, FileNotFoundError):
        messagebox.showinfo(title=website, message="Entry not found.")
    else:
        pyperclip.copy(password)
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\nPassword copied to clipboard.\n")


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n"
                                               f"Is is okay to save?")

        if is_ok:
            try:
                # Reading old data.
                with open(JSON_VAULT, "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                # Creating the file with the new data.
                with open(JSON_VAULT, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data.
                data.update(new_data)
                # Saving updated data.
                with open(JSON_VAULT, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
# Canvas
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(column=2, row=1)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)

# Labels
website_label = tkinter.Label(text="Website:", font=("aerial", 15, "normal"))
website_label.grid(column=1, row=2)

email_label = tkinter.Label(text="Email/Username:", font=("aerial", 15, "normal"))
email_label.grid(column=1, row=3)

password_label = tkinter.Label(text="Password:", font=("aerial", 15, "normal"))
password_label.grid(column=1, row=4)

# Entries
website_entry = tkinter.Entry(width=25)
website_entry.grid(column=2, row=2)
website_entry.focus()

email_entry = tkinter.Entry(width=45)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "info@necrux.com")

password_entry = tkinter.Entry(width=25)
password_entry.grid(column=2, row=4)

# Buttons
search_button = tkinter.Button(text="Search", command=search, width=16)
search_button.grid(column=3, row=2)

generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=4)

add_button = tkinter.Button(text="Add", highlightthickness=0, width=42, command=save)
add_button.grid(column=2, row=5, columnspan=2)
window.mainloop()
