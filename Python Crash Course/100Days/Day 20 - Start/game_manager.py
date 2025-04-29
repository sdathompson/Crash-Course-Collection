import time
#constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class GameManager:
    def __init__(self, snake_body, snake_screen):
        super(GameManager,self).__init__()
        self.game_is_on = True
        self.snake_body = snake_body # Store reference to SnakeBody instance
        self.snake_screen = snake_screen
        self.head = snake_body.segments[0]



    def move_snake(self):
        self.snake_screen.tracer(0)
        while self.game_is_on:
            self.snake_screen.update()
            time.sleep(0.1)
            for seg_num in range(len(self.snake_body.segments) - 1, 0,  -1): #range(start, stop, step) - start of the snake, stop (tail) of the snake, step (idx) of the snake segments
                new_x = self.snake_body.segments[seg_num - 1].xcor() # Start at segment 0 and have segment 1 move on top of segment 0
                new_y = self.snake_body.segments[seg_num - 1].ycor()
                self.snake_body.segments[seg_num].goto(new_x, new_y)
            self.head.forward(20)

    def heading_up(self):
        if self.head.heading() != DOWN: # To disallow opposite movement
            self.head.setheading(UP)

    def heading_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def heading_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def heading_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def control_snake(self):
        self.snake_screen.listen()

        self.snake_screen.onkey(key="Up", fun=self.heading_up)
        self.snake_screen.onkey(key="Right", fun=self.heading_right)
        self.snake_screen.onkey(key="Down", fun=self.heading_down)
        self.snake_screen.onkey(key="Left", fun=self.heading_left)


