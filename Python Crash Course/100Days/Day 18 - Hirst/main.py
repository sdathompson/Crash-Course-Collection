import random
import turtle as t


# Aliasing a name - making a module name shorter
# import turtle as t
# t.Class()

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

# TODO: Draw a square

def square():
    for idx in range(4):
        tim.forward(100)
        tim.right(90)

# TODO: Draw a dashed line

def dashed_line():
    for idx in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

# TODO: Draw a shape, increasing in side numbers by 1 each loop
#  Each side is 100 paces in length
#  Each shape is 360 / num of sides

def draw_shape(num_sides):
    angle = 360 / num_sides
    for idx in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# for shape_sides_n in range(3, 11):
#     tim.color(random.choice(colors))
#     # draw_shape(shape_sides_n) - Execution

# TODO: Random walk - thicker lines, random colors, faster speed
heading = [90, 0, 270, 180]
def random_walk(head):
    tim.pensize(10)
    tim.speed("fastest")
    tim.seth(random.choice(head))

# # Execution
# for i in range(200):
#         tim.color(random_color())
#         random_walk(heading)
#         tim.forward(20)

#TODO: Make a spirograph - rotate on the spot and draw 100r circles

def spirograph(gap):
    tim.speed("fastest")
    for i in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + gap)

# spirograph(5)

screen.exitonclick()









