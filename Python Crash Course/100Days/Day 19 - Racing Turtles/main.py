from turtle import Turtle, Screen
import random

# tim = Turtle()
# screen = Screen()
# starting_pos = tim.pos()
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.back(10)
#
#
# def move_cc():
#     tim.left(10)
#
#
# def move_c():
#     tim.right(10)
#
# def clear_screen():
#     tim.clear()
#     tim.teleport(starting_pos[0], starting_pos[1])
#     tim.seth(0)
#
#
#
# def movement():
#     screen.listen()
#     screen.onkey(key="Up", fun=move_forwards)
#     screen.onkey(key="Down", fun=move_backwards)
#     screen.onkey(key="Left", fun=move_cc)
#     screen.onkey(key="Right", fun=move_c)
#     screen.onkey(key="c", fun=clear_screen)
#
# movement()
# screen.exitonclick()

#TODO: Turtle Race


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

y_pos = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtle = []


for turtle_idx in range(0, 5):
    new_turtle = Turtle(shape="turtle", )
    new_turtle.penup()
    new_turtle.color(colors[turtle_idx])
    new_turtle.goto(x=-230, y=y_pos[turtle_idx])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:



    for turtle in all_turtle:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost :( the {winning_color} turtle is the winner.")
        random_move = random.randint(0,10)
        turtle.forward(random_move)

screen.exitonclick()


#TODO: Ask who will win the race?


