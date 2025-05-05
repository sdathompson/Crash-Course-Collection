from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POS = [(-40, 0), (-20, 0), (0,0)]

class SnakeBody(Turtle):
    def __init__(self, snake_screen, score_board, food_node):
        super().__init__(snake_screen, score_board, food_node)
        self.snake_screen = snake_screen
        self.food_node = food_node
        self.score_board = score_board
        self.game_is_on = True
        self.segments = [] # List to store segment of the snake
        self.create_snake()
        self.head = self.segments[0]  # Create a new RawTurtle instance

    def create_snake(self):
        for position in STARTING_POS:
            self.add_tail(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0,-1):  # range(start, stop, step) - start of the snake, stop (tail) of the snake, step (idx) of the snake segments
            new_x = self.segments[seg_num - 1].xcor()  # Start at segment 0 and have segment 1 move on top of segment 0
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
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


    def add_tail(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)  # Move segment to the starting position
        self.segments.append(new_segment)  # Add the segment to the list

    def extend(self):
        self.add_tail(self.segments[-1].pos())

    def food_collision(self):
        if self.head.distance(self.food_node) < 15:
            self.food_node.refresh()
            self.extend()
            self.score_board.increase_score()

    def wall_collision(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            self.game_is_on = False
            self.score_board.game_over()









