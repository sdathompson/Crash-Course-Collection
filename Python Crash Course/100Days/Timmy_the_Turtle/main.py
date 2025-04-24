# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkOrange1")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

from lists import gen1_pokemon
from lists import pokemon_types

table = PrettyTable()



table.add_column("Pokemon Name", gen1_pokemon)
table.add_column("Pokemon Types", pokemon_types)

table.align = "l"

print(table)