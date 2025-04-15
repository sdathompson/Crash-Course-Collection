print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: \n"))

#Nested If/Else conditions

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: \n"))
    if age < 12:
        print("You have the full discount: $5")
    elif age <= 18:
        print("You have a teen's discount. The ride is $7")
    else:
        print("The ride is the adult price of $18")
else:
    print("Sorry you have to grow taller before you can ride.")

