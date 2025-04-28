import colorgram
from colorgram import Color
import turtle as t
import random

colors = colorgram.extract('Hirst.jpg', 80)

# c_code = []
#
#
# for dots in colors:
#     r = dots.rgb.r
#     g = dots.rgb.g
#     b = dots.rgb.b
#     new_color = (r, g, b)
#     c_code.append(new_color)

#TODO: Paint a painting with 10 * 10 rows of 20r spots with a gap of 50
tim = t.Turtle()
scr = t.Screen()
tim.speed("fastest")
start_pos = tim.pos()
tim.teleport(-300, -300)
t.colormode(255)

colors_list = [(208, 160, 81), (55, 88, 130), (144, 91, 40), (140, 27, 48), (221, 207, 106), (133, 177, 203),
               (44, 54, 104), (157, 46, 85), (129, 189, 143), (164, 161, 37), (83, 21, 44), (187, 92, 104),
               (41, 42, 61), (186, 140, 170), (85, 123, 181), (79, 153, 164), (58, 39, 31), (87, 157, 91),
               (161, 201, 220), (194, 80, 73), (46, 74, 77), (80, 73, 44), (53, 131, 130), (217, 176, 189),
               (168, 207, 169), (178, 188, 213), (221, 180, 169), (46, 75, 74), (144, 39, 37), (47, 67, 63)]

def hirst_painting():
    for idx in range(10):
        rand_tup = random.choice(colors_list)
        tim.penup()
        tim.forward(50)
        tim.dot(20, rand_tup)


for _ in range(9):
    line_start = tim.pos()
    hirst_painting()
    tim.teleport(line_start[0],line_start[1] + 50)


hirst_painting()
tim.hideturtle()
scr.exitonclick()








