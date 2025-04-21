#TODO: logo and welcome
from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
#TODO: Choose a difficulty: Easy has 10 attempts and hard has 5
def set_game():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == 'easy':
        return 10
    elif diff == 'hard':
        return 5
    else:
        print("Invalid. Defaulting to easy")
        return 10

#TODO: Make a guess, if it's too high, print "too high" and guess again
# If it's too low, print "too low" and guess again.
def random_number():
    num_to_guess = random.randint(1,100)

    attempts_cnt = set_game()

    while attempts_cnt > 0:
        print(f"You have {attempts_cnt} attempts remaining to guess the number.")
        ask_guess = int(input("Make a guess: \n"))
        if ask_guess > num_to_guess:
            print("Too high.\nGuess again.")
        elif ask_guess < num_to_guess:
            print("Too low.\nGuess again.")
        elif ask_guess == num_to_guess:
            print(f"You got it! The answer was {num_to_guess}.")
            return
        elif attempts_cnt == 0:
            print("You've run out of guesses, you lose.")
        attempts_cnt -= 1

random_number()