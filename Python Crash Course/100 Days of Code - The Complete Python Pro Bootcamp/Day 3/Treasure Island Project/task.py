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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

Left_Right = input("You reach a fork in the road. "
                   "\n Do you want to go left down a well-trampled road or right through a dense thicket?: \n")
if Left_Right == "Left":
    Swim_Wait = input("You trudge through the jungle until you reach an aggressively flowing river."
                  "\n Did you want to try to swim across or wait to discover another solution?: \n")
    elif Left_Right == "Right":
    print("You push through the jungle as best you can without a machete."
        "\n Unfortunately, you don't see an old WWII pit trap before you and fall to your grisly demise. "
        "\nGame Over")
    if Swim_Wait == "Wait":
        Door = input("It leads to a room with five different coloured doors - Red, Blue, Green, Yellow, and Purple. "
                    "\n Which one do you open?: \n")
        if Door == "Red":
            print("Burned by fire. Game Over.")
        elif Door == "Blue":
            print("Eaten by beasts. Game over.")
        elif Door == "Yellow":
            print("You Win!")
else:
    print("Game Over.")




