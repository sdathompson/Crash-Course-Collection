import time
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
    time.sleep(0.1)
    screen.update()
#TODO: Set up random car generation
    car_spawner.drive()
    if car_spawner.xcor() <= 250:
        car_spawner.new_loc_col()
