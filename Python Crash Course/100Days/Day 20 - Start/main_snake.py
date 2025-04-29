from snake_body import SnakeBody
from snake_screen import SnakeScreen
from game_manager import GameManager


#TODO: Initialize screen

snake_screen = SnakeScreen()

#TODO: Create a snake body
snake_body =  SnakeBody(snake_screen)

game_manager = GameManager(snake_body, snake_screen)

#TODO: Control the snake - Initialize controls first
game_manager.control_snake()

#TODO: Move the snake
game_manager.move_snake()


#TODO: Detect collision with the food

#TODO: Create a scoreboard

#TODO: Detect collision with a wall

#TODO: Detect collision with tail


# Start the Tkinter mainloop with exit on click
snake_screen.start()
