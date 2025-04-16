print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

# todo: work out how much they need to pay based on their size choice.


# todo: work out how much to add to their bill based on their pepperoni choice.

# todo: work out their final amount based on whether if they want extra cheese.

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    print("That size doesn't exist.")

print(f"Your final bill is: ${bill}.")
