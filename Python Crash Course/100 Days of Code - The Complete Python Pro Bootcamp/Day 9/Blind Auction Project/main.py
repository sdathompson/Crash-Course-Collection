import os, platform
from art import logo



# TODO-1: Ask the user for input
other_users = True
print(logo)
auction = {}
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
while other_users:
    bidder_name = input("What is your name?:\n")
    bidder_price = int(input("What is your price?:\n"))
# TODO-2: Save data into dictionary {name: price}
    auction[bidder_name] = bidder_price
    print(auction)
# TODO-3: Whether if new bids need to be added
    new_bids_q = input("Do you want to add new bids? 'Y' for yes and 'N' for no:\n").lower()
# TODO-4: Compare bids in dictionary
    if new_bids_q == 'n':
        other_users = False
        highest_bidder = max(auction, key=auction.get)
        highest_price = auction[highest_bidder]
        print(f"The highest bidder is {highest_bidder} with a bid of ${highest_price}! Congratulations!")
    if new_bids_q == 'y':
        print("\n" * 20)
        # clear()


