from turtle import RawTurtle

class SnakeBody(RawTurtle):
    def __init__(self, screen ,shape="square", color="green", lead_x=-40,lead_y=0, stretch_wid=1, stretch_len=1):
        self.segments = [] # List to store segment of the snake
        self.starting_pos = [] # List to store starting positions
        super().__init__(screen)

        for _ in range(2):
            segment = RawTurtle(screen) #Create a new RawTurtle instance
            segment.teleport(lead_x, lead_y)  #Move segment to the starting position
            segment.penup()
            segment.shape(shape)
            segment.shapesize(stretch_wid, stretch_len)
            segment.color(color)

            self.segments.append(segment) #Add the segment to the list
            self.starting_pos.append(segment.pos()) #Add the segment position to the list
            lead_x += 20





