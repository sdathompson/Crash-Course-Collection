from tkinter import *
import math
from timer import Pomo

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_tick = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    # Stop the timer
    window.after_cancel(timer_tick)
    # Reset timer to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # Reset title to Timer (timer.config(text="Timer")
    timer.config(text="Timer")
    # Reset checkmarks
    check.config(text="")
    # Reset reps to 0
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    work_test = 3
    short_test = 2
    long_test = 5

    #If it's the 8th rep:
    if reps % 8 == 0:
        timer.config(text="Long Break", fg=RED)
        count_down(work_sec)
        reps = 0
    #If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        timer.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    #If it's the 1st/3rd/5th/7th rep:
    else:
        timer.config(text="Work Time", fg=GREEN)
        count_down(long_break_sec)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # Changing a canvas item is different than changing a text item

    # 1 min = 60 sec
    # Format count to display in 00:00
    # The minute portion: divide by 60 rounded down
    # The seconds portion: % 60
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_tick
        timer_tick = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0 and reps != 0:
            check.config(text=check.cget("text") + "🗸")
        elif reps == 0:
            check.config(text="")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
#Pomodoro is Tomato in Italian
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

rounded_rec = PhotoImage(file="Button.png")

init = Label(text="", bg=YELLOW)
init.grid(column=0, row=0)

# Timer Label
timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(column=1, row=0)
# width and height in pixel
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# PhotoImage to use a image on a canvas
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start and Reset Button
start = Button(text="Start", font=("Segoe UI", 10, "bold"), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2, pady=10)

reset = Button(text="Reset", font=("Segoe UI", 10, "bold"), highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2, pady=10)

# Checkmarks
check = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check.grid(column=1, row=3)

window.mainloop()