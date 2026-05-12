import pandas
import random
from tkinter import *
from gtts import gTTS
import pygame
import time
import os
import threading
from flashcard_window import FlashCardWindow
from language_config import LanguageConfig
from menu_window import MenuWindow

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

LANGUAGES = [
    LanguageConfig(
        display_name="Korean",
        lang_code="ko",
        bg_color=GREEN,
        flipped_bg_color=PINK,
        csv_path="./Korean - Japanese - English Flash Cards - Korean.csv",
        word_col="Korean",
        translation_col="Ko to En",
        temp_filename="korean_temp.mp3"
    ),
    LanguageConfig(
        display_name="Japanese",
        lang_code="ja",
        bg_color=BLUE,
        flipped_bg_color=BEIGE,
        csv_path="./Korean - Japanese - English Flash Cards - Japenese.csv",
        word_col="Japanese",
        translation_col="Ja to En",
        temp_filename="japanese_temp.mp3"
    ),
]

if __name__ == "__main__":
    MenuWindow(languages=LANGUAGES).run()
