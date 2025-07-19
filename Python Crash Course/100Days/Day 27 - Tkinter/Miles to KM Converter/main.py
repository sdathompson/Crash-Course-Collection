from tkinter import *
import math

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
# window.config(padx=10, pady=10)

init = Label(text="", padx=30, pady=5)
init.grid(column=0, row=0)

#TODO: Needs a entry field with "Miles" label beside it
miles_input = Entry()
miles_input.grid(column=1, row=1)
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=1)

#TODO: Needs a label "is equal to" in column 0 and row 1
equal_input = Label(text="is equal to", font=("Arial", 12))
equal_input.grid(column=0, row=2, padx=10)

#TODO: Needs a level that starts at 0 and changes to a conversion of miles everytime
calc = Label(text="0", font=("Arial", 12))
calc.grid(column=1, row=2)

km = Label(text="Km", font=("Arial", 12))
km.grid(column=2, row=2)

#TODO: Button that takes the input of miles_input and calculates a miles-km conversion
def miles_to_km():
    conversion = round(int(miles_input.get()) * (80467/50000), 2)
    calc.config(text=conversion)

con_button = Button(text="Calculate", command=miles_to_km)
con_button.grid(column=1,row=3)


window.mainloop()