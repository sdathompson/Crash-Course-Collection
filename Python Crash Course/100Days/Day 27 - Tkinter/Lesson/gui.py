# Tkinter - History of a GUI (Graphical User Interface)
# Tkinter has three methods to initialize parts of the interface: pack, place, and grid
# Movie - Pirates of Silicon Valley

from tkinter import *
import random

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    label.config(text=inp.get())

def button_clicked2():
    random_inp = [random.choice(inp.get()) for _ in range(len(inp.get()))]
    random_join = "".join(random_inp)
    label.config(text=random_join)
#Label

label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# Pack starts at the top and packs subsequent packs underneath
# Place defines a coordinate to place the widget
# Grid divides the program into
label.grid(column=0, row=0)


button = Button(text="Click Me!", command=button_clicked)
button.grid(column=2, row=1)

new_button = Button(text="Press Me!", command=button_clicked2)
new_button.grid(column=3, row=0)

# Entry - enter text

inp = Entry()
inp.grid(column=4, row=3)

# Text Entry Box

# Spinbox (Counter)

# Scale(Slider)

# Checkbutton (Checkbox)

# Radiobutton (One option list)

# Listbox (Multiple option list)

window.mainloop()




