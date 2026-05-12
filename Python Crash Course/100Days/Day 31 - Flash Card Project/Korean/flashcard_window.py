from tkinter import Tk, Canvas, Label, Button, PhotoImage

from language_config import LanguageConfig
from tts_speaker import TTSSpeaker
from word_picker import WordPicker

GREEN = "#A8D5C5"
PINK = "#D57E7E"
BLUE = "#A2CDCD"
BEIGE = "#FFE1AF"

class FlashCardWindow:
    def __init__(self, config: LanguageConfig):
        self.config = config
        self.speaker = TTSSpeaker(lang=config.lang_code, temp_filename=config.temp_filename)
        self.picker = WordPicker(
            csv_path=config.csv_path,
            word_col=config.word_col,
            translation_col=config.translation_col
        )
        self._score = 0
        self._flipped = False

        self.window = Tk()
        self.window.title(f"Learn {config.display_name}!")
        self.window.config(padx=50, pady=50, bg=config.bg_color)
        self._build_ui()


    def _build_ui(self):
        # Flash card canvas
        self._card_img = PhotoImage(file="./Images/card_front.png")
        self._canvas = Canvas(
            self.window, bg=self.config.bg_color,
            width=800, height=526, highlightthickness=0
        )
        self._canvas.create_image(400, 263, image=self._card_img)
        self._canvas.grid(columnspan=2, column=0, row=0)
        self._canvas.bind("<Button 1>", self._flip_card)
        self._score_number = Label(
            self.window,
            text=f"{self._score}",
            font=("Arial", 20),
            borderwidth=1,
            bg=self.config.bg_color
        )
        self._score_number.grid(column=0, row=3, columnspan=2)
        self._flipped = False

        # Language label
        Label(
            self._canvas,
            text=self.config.display_name,
            font=("Arial", 40, "italic"),
            bg="white"
        ).place(relx=0.5, rely=0.30, anchor="center")

        # Word label
        self._word_label = Label(
            self._canvas,
            text="",
            font=("Arial", 60, "bold"),
            bg="white"
        )
        self._word_label.place(relx=0.5, rely=0.60, anchor="center")

        # Translation label (hidden until card is flipped)
        self._translation_label = Label(
            self._canvas,
            text="",
            font=("Arial", 20),
            bg=self.config.bg_color,
            fg="grey"
        )
        self._translation_label.place(relx=0.5, rely=0.80, anchor="center")

        # Buttons
        self._cross_img = PhotoImage(file="./Images/wrong.png")
        cross_button = Button(
            self.window, image=self._cross_img,
            highlightthickness=0, command=self.next_word
        )
        cross_button.grid(column=0, row=3)


        self._check_img = PhotoImage(file="./Images/right.png")
        check_button = Button(
            self.window, image=self._check_img,
            highlightthickness=0, command=self._update_score
        )
        check_button.grid(column=1, row=3)

        # Score
        score_label = Label(
            self.window,
            text="Score",
            font=("Arial", 20),
            bg=self.config.bg_color,
        )
        score_label.grid(column=0, row=1, columnspan=2)

    def next_word(self):
        """Pick a new random word, update the UI, and speak it."""
        word, translation = self.picker.random_pair()
        self._word_label.config(text=word, bg="white")
        self._translation_label.config(text="*Click to reveal*", bg=self.config.bg_color, fg="grey")
        self._flipped = False
        self.speaker.speak(word)

    def _flip_card(self, event=None):
        if self._flipped:
            self._translation_label.config(
                text="*Click to reveal*",
                bg=self.config.bg_color,
                fg="grey"
            )
            self._word_label.config(bg="white")
            self._flipped = False
        else:
            _, translation = self.picker.last_pair()
            self._translation_label.config(
                text=translation,
                bg=self.config.flipped_bg_color,
                fg="black"
            )
            self._word_label.config(bg=self.config.flipped_bg_color)
            self._flipped = True

    def _update_score(self):
        self.next_word()
        self._score += 1
        self._score_number.config(text=str(self._score))

    def run(self):
        self.next_word()
        self.window.mainloop()