from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def spawn_point_choice(spawn_point):
    spawn_point = random.randint(a=-150, b=200)
    return spawn_point


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.y_spawn = random.randint(a=-150, b=200)
        self.random_colors = random.choice(COLORS)
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(self.random_colors)
        self.goto(x=250, y=self.y_spawn)
        self.move_dis = STARTING_MOVE_DISTANCE

    def new_loc_col(self):
        self.random_colors = random.choice(COLORS)
        self.goto(x=280, y=spawn_point_choice(self.y_spawn))

    def color_choice(self):
        self.random_colors = random.choice(COLORS)
        return self.random_colors

    def drive(self):
        new_x = self.xcor() - self.move_dis
        self.setpos(new_x, self.y_spawn)

