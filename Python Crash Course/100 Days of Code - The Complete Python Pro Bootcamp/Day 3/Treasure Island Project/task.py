print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


def game_over(reason):
    print(f"{reason} Game Over.")


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

Left_Right = input(
    "You reach a fork in the road.\nDo you want to go 'Left' down a well-trampled road or 'Right' through a dense thicket? \n").capitalize()

if Left_Right == "Left":
    Swim_Wait = input(
        "You trudge through the jungle until you reach an aggressively flowing river.\nDo you want to 'Swim' across or 'Wait' to discover another solution? \n").capitalize()

    if Swim_Wait == "Wait":
        Door = input(
            "You find a room with five doors - Red, Blue, Green, Yellow, and Purple.\nWhich one do you open? \n").capitalize()

        if Door == "Yellow":
            print("You open the Yellow door and find the treasure! You Win!")
        elif Door == "Red":
            game_over("Burned by fire.")
        elif Door == "Blue":
            game_over("Eaten by beasts.")
        elif Door == "Green" or Door == "Purple":
            game_over("The door leads to nothingness.")
        else:
            game_over("Invalid choice.")
    else:
        game_over("You try to swim across but are swept away by the current into some rocks.")

elif Left_Right == "Right":
    game_over("You fall into a hidden WWII pit trap.")
else:
    game_over("You took too long to decide.")



