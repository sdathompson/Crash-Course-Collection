FONT = ("Courier", 24, "normal")
from turtle import Turtle
import pandas

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.guessed_states = set()
        self.missing_states = []



