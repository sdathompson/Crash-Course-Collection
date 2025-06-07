from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(0, -250)
        self.shape("turtle")
        self.go_forwards()

    def go_forwards(self):
        turtle_crawl = self.ycor() + 10
        self.goto(x=self.xcor(), y=turtle_crawl)
