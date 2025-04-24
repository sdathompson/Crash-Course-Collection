#TODO: print the logo

#import random module
import random
from art import logo
print(logo)

#TODO: 1. Initialize the table dictionary: User hand, Computer hand, and Deck.

# To access: for key in dictionary:
# dictionary[key] = value
# key = key
table = {
    "User": [],
    "CPU": [],
    "Deck": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
}
def score():
    user_scr = sum(table["User"])
    cpu_scr = sum(table["CPU"])
    return user_scr, cpu_scr

def win_lose():
# if not, compare user score with computer score to see if user score is higher.
# if user score is lower, user loses. If scores are the same, they draw, and if user score is higher, user wins.
    if score()[1] > 21 or score()[0] == 21 or score()[0] > score()[1]:
        print("You win :)")
    elif score()[0] > 21 or score()[0] < score()[1]:
        print("You lose :(")
    elif score()[0] == score()[1]:
        print("It's a draw :/")

def immediate_blackj():
    if score()[0] == 21:
        print("You win :)")
    if score()[1] == 21:
        print("You lose :(")

def bust_check():
    if score()[1] > 21 or score()[0] == 21:
        print("You win :)")
    elif score()[0] > 21 or score()[1] == 21:
        print("You lose :(")

def random_card():
    card = random.choice(table["Deck"])
    return card

def deal():

#TODO: 2. Give both the user and computer 2 random cards.
# The user sees both of their cards but one CPU card is hidden
    for player in table:
        while len(table[player]) < 2:
            random_card()
            table[player].append(random_card())
    print(f"    Your cards: {table["User"]}, current score: {score()[0]}")
    print(f"    Computer's first card: {table["CPU"][0]}")

#TODO: 3. Immediate blackjack check
    immediate_blackj()

    hit_me = True
    while hit_me:
    #TODO: 4. Ace check
        if score()[0] > 21:
            for card in range(len(table["User"])):
                if table["User"][card] == 11:
                    table["User"][card] = 1
    # if the user's score is not over 21, ask the user if they want another card.
#TODO: 5. If the user wants another card, loop back to step 3.
        if score()[0] < 21:
            hit = input("\nType 'y' to get another card and 'n' to pass:").lower()
            if hit == 'n':
                hit_me = False
# If not, the computer plays a loop as long as it's score is less than 17.
#TODO: 6. If the computer has gone over 21, users wins.
                while score()[1] < 17:
                    table["CPU"].append(random_card())
                print(f"CPU's hand: {table["CPU"]}  CPU's score: {score()[1]}\nUser's hand: {table["User"]}  User's score: {score()[0]}")
                win_lose()
            if hit == 'y':
                table["User"].append(random_card())
                print(f"User's hand: {table["User"]}  User's score: {score()[0]}")
                bust_check()



deal()









