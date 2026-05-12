from tkinter import Tk, Label, Button, PhotoImage, Frame

from language_config import LanguageConfig
from flashcard_window import FlashCardWindow


class MenuWindow:
    def __init__(self, languages: list[LanguageConfig]):
        self.languages = languages
        self.root = Tk()
        self.root.title("Choose a language")
        self._build_ui()

    def _build_ui(self):
        Label(text="").grid(column=0, row=0)

        self._person_img = PhotoImage(file="./Images/Person.png")
        Label(self.root, image=self._person_img).grid(column=1, row=0)

        Label(
            self.root,
            text="What language do you want to learn?",
            font=("Segoe UI", 24, "bold"),
            justify="center",
            pady=10,
            padx=10
        ).grid(column=1, row=1)

        # Dynamically build a button for each language
        button_frame = Frame(self.root)
        button_frame.grid(column=0, row=2, columnspan=3, pady=10)
        for config in self.languages:
            Button(
                button_frame,
                text=config.display_name,
                padx=10,
                command=lambda c=config: self._launch(c)
            ).pack(side="left", padx=10)

    def _launch(self, config: LanguageConfig):
        self.root.destroy()
        FlashCardWindow(config).run()

    def run(self):
        self.root.mainloop()
