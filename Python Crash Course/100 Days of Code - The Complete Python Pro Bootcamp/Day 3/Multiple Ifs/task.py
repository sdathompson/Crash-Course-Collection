print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: \n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: \n"))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age < 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photos = str(input("Do you want photos? Y for Yes and N for no: \n"))
    if wants_photos == "Y":
        print("Photos are an extra $3")
        bill += 3
    elif wants_photos == "N":
        print("No photos have been purchased")
    else:
        print("Invalid Selection for Photo")

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")