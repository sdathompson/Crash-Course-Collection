from turtle import Turtle
import player
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = [] # List to store car objects
        self.move_dis = STARTING_MOVE_DISTANCE
        self.move_speed = 0.1
        self.active = True
        self.hideturtle()


    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(x=400, y=random.randint(-150, 200))
        self.cars.append(new_car)

    def drive(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_dis
            car.setpos(new_x, car.ycor())

    def stop(self):
        self.active = False


