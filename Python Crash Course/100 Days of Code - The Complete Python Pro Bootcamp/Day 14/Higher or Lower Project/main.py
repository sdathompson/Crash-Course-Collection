import art
from game_data import data
import random
import sys

#TODO: Compare one {name}, a {description}, from {country} to another.
# Print ASCII art in between

print(art.logo)
# Clear console between each
comparison = {
    "listA": [],
    "listB": [],
}
current_scr = 0

def win():
    global current_scr

    current_scr += 1
    print("\n" * 20)
    comparison["listA"] = []
    comparison["listB"] = []
    print(art.logo)
    return f"You're right ! Current score: {current_scr}"

def lose():
    global current_scr
    print("\n" * 20)
    print(art.logo)
    return f"Sorry that's incorrect! Final score: {current_scr}"

def random_grabs(score):
    global current_scr
    correct_guess = True

    while correct_guess:

#Iterate through the

        for items in comparison:
                rand_data_idx = random.randint(1, (len(data) - 1))
                name_str = ' '.join(data[rand_data_idx]['name'].split())
                comparison[items].append(name_str)
                desc_str= ' '.join(data[rand_data_idx]['description'].split())
                comparison[items].append(desc_str)
                cntry_str= ' '.join(data[rand_data_idx]['country'].split())
                comparison[items].append(cntry_str)
                follow_cnt = data[rand_data_idx]['follower_count']
                comparison[items].append(follow_cnt)

# Checks to see if rand_data_idx pulled a duplicate entry. If it did, re-run the function
# Checks for an inequality in both followings (can't compare if they have the same amount of followers)

        follow_a = comparison["listA"][3]
        follow_b = comparison["listB"][3]

        if comparison["listA"] != comparison["listB"] and follow_a != follow_b:
            print(f"Compare A: {comparison["listA"][0]}, a {comparison["listA"][1]}, from {comparison["listA"][2]}.")
            print(f"\n{art.vs}\n")
            print(f"Against B: {comparison["listB"][0]}, a {comparison["listB"][1]}, from {comparison["listB"][2]}")
        else:
            random_grabs(score)

#TODO: Guess who has more followers: A or B?


        guess = input("Who has more followers? Type 'A' or 'B': ").upper()


    # If guess is right, add to score and pull another comparison
        if guess == 'A':
            if follow_a > follow_b:
                print(win())
                random_grabs(current_scr)
    # If guess is wrong, clear screen and print a game over message with the final score
            elif follow_a < follow_b:
                print(lose())
                correct_guess = False
                sys.exit()
        if guess == 'B':
            if follow_a < follow_b:
                print(win())
                random_grabs(current_scr)
            elif follow_a > follow_b:
                print(lose())
                correct_guess = False
                sys.exit()

random_grabs(current_scr)

#dictionaries inside a list
#To call a value: use list[idx]['key']


