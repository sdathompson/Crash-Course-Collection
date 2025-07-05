import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy")
screen.tracer(0)

#TODO: Turtle player character init
turtle_player = Player()
car_spawner = CarManager()
level_cnt = Scoreboard()

#TODO: Set up random color picker


#TODO: Set up turtle player movement
screen.listen()
screen.onkey(fun=turtle_player.go_forwards, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(car_spawner.move_speed)
    screen.update()
#TODO: Set up random car generation
    if random.randint(1, 6) == 1: # The lower the range, the more frequent cars spawn
        car_spawner.create_car()

#TODO: Set up turtle-car collision
    for traffic in car_spawner.cars:
        if turtle_player.distance(traffic) < 20:
            screen.onkey(None, "Up")
            level_cnt.game_over()
            car_spawner.move_dis = 0

    car_spawner.drive()

#TODO: Set up finish
    if turtle_player.finish():
        turtle_player.reset()
        car_spawner.move_speed -= 0.05
        level_cnt.increase()

