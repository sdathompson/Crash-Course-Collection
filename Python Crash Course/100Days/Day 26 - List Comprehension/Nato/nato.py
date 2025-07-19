import pandas

class Nato:
    def __init__(self):
        self.nato_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
        self.nato_alphabet = {row.letter:row.code for (index, row) in self.nato_frame.iterrows()}
