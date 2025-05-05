import time

from snake_body import SnakeBody
from game_manager import GameManager
from scoreboard import Scoreboard
from turtle import Screen
from food import Food

game_is_on = True

#TODO: Initialize screen
snake_screen = Screen()

#TODO: Create a snake body

# Create food
food_node = Food()
#Create scoreboard
score_board = Scoreboard()

snake_body =  SnakeBody(food_node=food_node, score_board=score_board, snake_screen=snake_screen)
game_manager = GameManager(snake_body, snake_screen, food_node, score_board)


#TODO: Move the snake
while game_is_on:
    snake_screen.update()
    time.sleep(0.1)
    snake_body.move()

#TODO: Control the snake - Initialize controls first
snake_body.control_snake()
#TODO: Detect collision with the food
#TODO: Create a scoreboard
snake_body.food_collision()

#TODO: Detect collision with a wall

#TODO: Detect collision with tail

snake_screen.exitonclick()
