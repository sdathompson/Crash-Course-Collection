import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for char_l in range(1, nr_letters+1):
    rnd_letters = str(random.choice(letters).lower())
    password += rnd_letters
for char_s in range(1, nr_symbols+1):
    rnd_symbols = random.choice(symbols)
    password += rnd_symbols
for char_n in range(1, nr_numbers+1):
    rnd_numbers = random.choice(numbers)
    password += rnd_numbers

password_shuffle = ''.join(random.sample(password,len(password)))

print(f"Your generated password is: {password_shuffle}")



