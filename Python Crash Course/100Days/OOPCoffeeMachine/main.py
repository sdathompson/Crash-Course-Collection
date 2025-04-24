import sys

from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from sys import exit

#TODO: Prompt user ("What would you like? (espresso/latte/cappuccino):")
# Check user input to decide what to do next
match_order = Menu()
money_time = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

def process():
    print("Welcome to the Coffee Machine!")
    coffee_order = input("What would you like? (espresso/latte/cappuccino): ")
    enough_order = True

    if coffee_order == "off":
        print("Rebooting coffee machine...")
        process()

    if coffee_order == "report":
        coffee_maker.report()
        money_time.report()
        exit()

    for n_idx in match_order.menu:
        # Check if there are enough resources to make the drink
        enough_order = coffee_maker.is_resource_sufficient(n_idx)
        if not enough_order:
            process()

    #Process coins
    deposit = money_time.process_coins()
    # Check if the transaction is successful
    money_time.make_payment(deposit)
    process()
process()