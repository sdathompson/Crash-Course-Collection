import time

#constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POS = [(-40, 0), (-20, 0), (0,0)]

class GameManager:
    def __init__(self, snake_body, snake_screen, food_node, score_board):
        super().__init__()
        # References to other classes
        self.snake_body = snake_body
        self.snake_screen = snake_screen
        self.food_node = food_node
        self.score_board = score_board
        self.head = self.snake_body

        self.snake_screen.setup(width=600, height=600)  # Screen Setup
        self.snake_screen.bgcolor("black")
        self.snake_screen.title("My Snake Game")
        self.snake_screen.tracer(0)

        # Detect head collision with wall






