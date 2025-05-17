from turtle import Turtle
import random

MOVE_DIS = 20

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)

        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def rebound(self):
        self.x_move *= -1