from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
#TODO: 9. Set up scoreboard class
pong_score = Scoreboard()

# TODO: 3. Set up movement of paddles
pong_screen.listen()
pong_screen.onkey(fun=r_paddle.go_up, key="Up")
pong_screen.onkey(fun=r_paddle.go_down, key="Down")

pong_screen.onkey(fun=l_paddle.go_up, key="w")
pong_screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    pong_screen.update()
# TODO: 5. Set up movement for ball
    pong_ball.move()

# TODO: 6. Detect collision with top and bottom walls and bounce
#  Change the ball's movement direction upon collision
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce()

# TODO: 7. Detect collision with paddles
# Right paddle collision
    if pong_ball.distance(r_paddle) < 40 and pong_ball.xcor() > 320:
        pong_ball.rebound()
# Left paddle collision
    elif pong_ball.distance(l_paddle) < 40 and pong_ball.xcor() < - 320:
        pong_ball.rebound()

#TODO: 8. Detect if the ball goes out of bounds at the edge of the screen.
    # Right paddle misses
    if pong_ball.xcor() > 380:
    # If yes, reset the ball's position to the center of the screen.
    # The ball should then start moving towards the other player
# TODO: 9. Add to score when the paddle misses the ball
        pong_score.l_increase()
        pong_ball.reset_position()

    # Left paddle misses
    if pong_ball.xcor() < -380:
        pong_score.r_increase()
        pong_ball.reset_position()
        pong_ball.move_speed = 0.1


pong_screen.exitonclick()