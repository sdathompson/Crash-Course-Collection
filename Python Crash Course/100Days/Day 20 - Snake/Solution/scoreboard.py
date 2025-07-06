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
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write(GAME_OVER, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()
       