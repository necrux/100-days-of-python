#!/usr/bin/env python3
import tkinter

MILE_TO_KILOMETER = 1.609344


def kilo_converter():
    miles = float(miles_input.get())
    km = round(miles * MILE_TO_KILOMETER, 2)
    conversion.config(text=km)


# Build window.
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=30, pady=30)

# Labels.
is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_label.grid(column=1, row=2)

miles_label = tkinter.Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=3, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=3, row=2)

# Numbers.
conversion = tkinter.Label(text="0", font=("Arial", 10, "bold"))
conversion.grid(column=2, row=2)

miles_input = tkinter.Entry(width=5)
miles_input.grid(column=2, row=1)

# Button.
calculate = tkinter.Button(text="Calculate", command=kilo_converter)
calculate.grid(column=2, row=3)

window.mainloop()
