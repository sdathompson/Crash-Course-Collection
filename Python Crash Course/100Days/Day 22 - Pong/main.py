from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


# TODO: 1. Create screen
pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.bgcolor("black")
pong_screen.title("Pong Game")
pong_screen.tracer(0)


# TODO: 2. Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# TODO: 4. Set up ball class
pong_ball = Ball((0, 0))

# TODO: 3. Set up movement of paddles
pong_screen.listen()
pong_screen.onkey(fun=r_paddle.go_up, key="Up")
pong_screen.onkey(fun=r_paddle.go_down, key="Down")

pong_screen.onkey(fun=l_paddle.go_up, key="w")
pong_screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    pong_screen.update()
# TODO: 5. Set up movement for ball
    pong_ball.move()

# TODO: 6. Detect collision with top and bottom walls and bounce
#  Change the ball's movement direction upon collision
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce()

# TODO: 7. Detect collision with paddle
    if r_paddle.distance(pong_ball) < 20 or l_paddle.distance(pong_ball) < 20:
        pong_ball.rebound()

# TODO: 8. Add to score when the paddle misses the ball

pong_screen.exitonclick()