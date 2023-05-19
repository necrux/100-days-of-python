#!/usr/bin/env python3
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
label1 = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
label1.grid(column=1, row=1)

# Button


def button_clicked():
    label1.config(text=input1.get())


button1 = tkinter.Button(text="Click Me", command=button_clicked)
button1.grid(column=2, row=2)

button2 = tkinter.Button(text="Button 2")
button2.grid(column=3, row=1)

# Entry
input1 = tkinter.Entry(width=10)
input1.grid(column=4, row=3)


window.mainloop()
