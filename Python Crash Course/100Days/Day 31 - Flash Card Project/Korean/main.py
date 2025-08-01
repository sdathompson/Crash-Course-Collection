import pandas
import random
from tkinter import *

GREEN = "#A8D5C5"
PINK = "#D57E7E"
BLUE = "#A2CDCD"
BEIGE = "#FFE1AF"

# Flash Card Program - Time to learn Korean

# Check the wiki for the most frequently used words in other languages - https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800
# Check HermitDave for usable language files - https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
# Language Codes for Google Translate - https://cloud.google.com/translate/docs/languages?hl=en
# Taking a .txt file and converting it to a .csv
# Japanese
# ja_to_csv = pandas.read_csv("D:/Work/Crash Course Collection/Python Crash Course/100Days/Day 31 - Flash Card Project/ja_50k.txt", sep=' ')
# ja_to_csv.to_csv('output_ja.csv', index=False)

# Korean
# ko_to_csv = pandas.read_csv("D:/Work/Crash Course Collection/Python Crash Course/100Days/Day 31 - Flash Card Project/ko_50k.txt", sep=' ')
# ko_to_csv.to_csv('output_ko.csv', index=False)

ko_pandas = pandas.read_csv("./Korean - Japanese - English Flash Cards - Korean.csv")
ko_df = pandas.DataFrame(ko_pandas)
ko_df_selected = ko_df[['Korean', 'Ko to En']]

ja_pandas = pandas.read_csv("./Korean - Japanese - English Flash Cards - Japenese.csv")
ja_df = pandas.DataFrame(ja_pandas)
ja_df_selected = ja_df[['Japanese', 'Ja to En'
                                    '']]




def open_ko_window():
    root_menu.destroy()

    ko_window = Tk()
    ko_window.title("Learn Korean!")
    ko_window.config(padx=50, pady=50, bg=GREEN)

    # Front Image
    flash_card_img = PhotoImage(file="./Images/card_front.png")
    flash_card_canvas = Canvas(ko_window, bg=GREEN, width=800, height=526, highlightthickness=0)
    flash_card_canvas.create_image(400, 263, image=flash_card_img)
    flash_card_canvas.grid(columnspan=2, column=0, row=0)

    # What language we're using
    ko_lbl = Label(text="Korean", font=("Ariel", 40, "italic"), bg="white")
    ko_lbl.place(x=300, y=150)

    # Select a random row
    ko_row = random.randint(0, ko_df_selected.shape[0])
    # Use .iat to find the exact row and column
    random_ko = ko_df_selected.iat[ko_row, 0]
    ko_wrd = Label(text=f"{random_ko}", font=("Ariel", 60, "bold"), bg="white")
    ko_wrd.place(x=300, y=263)

    # Buttons

    ko_window.mainloop()


def open_ja_window():
    root_menu.destroy()

    ja_window = Tk()
    ja_window.title("Learn Japanese!")


    ja_window.mainloop()


root_menu = Tk()
root_menu.title("Choose a language")

init = Label(text="")
init.grid(column=0, row=0)

ko_char_img = PhotoImage(file="./Images/Person.png")
ko_char_label = Label(root_menu, image=ko_char_img)
ko_char_label.grid(column=1, row=0)

main_label = Label(text="What language do you want to learn?", font=("Segoe UI", 24, "bold"), justify="center",pady=10, padx=10)
main_label.grid(column=1, row=1)

hangul_img = PhotoImage(file="./Images/Hangul.png")
hangul_label = Label(root_menu, image=hangul_img)
hangul_label.grid(column=1, row=2, sticky="w")

ko_button = Button(root_menu, text="Korean", padx=10, command=open_ko_window)
ko_button.grid(column=1, row=3, sticky="w")

kanji_img = PhotoImage(file="./Images/Kanji.png")
kanji_label = Label(root_menu, image=kanji_img)
kanji_label.grid(column=1, row=2, sticky="e")

ja_button = Button(root_menu, text="Japanese", padx=10, command=open_ja_window)
ja_button.grid(column=1, row=3, sticky="e")

root_menu.mainloop()
