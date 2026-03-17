import random
from tkinter import *
import pandas

# Currently, only the flip button works. The point system will be added later

#Color codes
GREEN = "#A8D5C5"
PINK = "#D57E7E"
BLUE = "#A2CDCD"
BEIGE = "#FFE1AF"

FlipItr = 0
current_card_img = None
current_question = ""
current_answer = ""

flashcard_pandas = pandas.read_csv("./FlashcardQA.csv")
flashcard_df = pandas.DataFrame(flashcard_pandas)

root_menu = Tk()
root_menu.title("Generative AI Developer Flashcards")
root_menu.config(padx=50, pady=50, bg=GREEN)

# Front Image
flash_card_img = PhotoImage(file="./Images/card_front.png")
flash_card_canvas = Canvas(root_menu, bg=GREEN, width=800, height=526, highlightthickness=0)
flash_card_canvas.create_image(400, 263, image=flash_card_img)
flash_card_canvas.grid(columnspan=3, column=0, row=0)

card_image_id = flash_card_canvas.create_image(400, 263, image=flash_card_img)

qst_wrd = Label(flash_card_canvas, text="", font=("Ariel", 12, "bold"), bg="white")
qst_wrd.place(relx=0.5, rely=0.60, anchor="center")

def rand_qa():
    #Select a random row
    qa_row = random.randint(0, flashcard_df.shape[0] - 1)
    random_qst = flashcard_df.iat[qa_row, 0]
    random_ans = flashcard_df.iat[qa_row, 1]
    return random_qst, random_ans

def flip_card():
    global current_card_img, FlipItr, current_question, current_answer

    FlipItr += 1

    if FlipItr % 2 == 0 and FlipItr != 0:
        current_card_img = PhotoImage(file="./Images/card_back.png")
        qst_wrd.config(text=current_answer, font=("Ariel", 14), bg=GREEN)
    else:
        current_question, current_answer = rand_qa()
        current_card_img = PhotoImage(file="./Images/card_front.png")
        qst_wrd.config(text=current_question, font=("Ariel", 20, "bold"), bg="white")

    flash_card_canvas.itemconfig(card_image_id, image=current_card_img)



# Buttons
cross_img = PhotoImage(file="./Images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=rand_qa)
cross_button.grid(column=0, row=1)

flip_img = PhotoImage(file="./Images/zulip-icon-128x128.png")
flip_button = Button(image=flip_img, highlightthickness=0, command=flip_card)
flip_button.grid(column=1, row=1)

check_img = PhotoImage(file="./Images/right.png")
check_button = Button(image=check_img, highlightthickness=-0, command=rand_qa)
check_button.grid(column=2, row=1)

root_menu.mainloop()





