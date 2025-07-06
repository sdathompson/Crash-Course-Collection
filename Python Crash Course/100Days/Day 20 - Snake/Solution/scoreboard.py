from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
GAME_OVER = "GAME OVER"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.teleport(0, 260)
        self.hideturtle()
        self.color("white")
        self.points = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.points}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(GAME_OVER, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.clear()
        self.update_scoreboard()
       