from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.go_forwards()

    def go_forwards(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset(self):
        self.goto(STARTING_POSITION)
