from machine import coins_amount
from machine import resources
from machine import MENU

# TODO: Input which coffee the user would like

money_lvl = 0


def report():
    global money_lvl
    water_lvl = int(resources["water"])
    milk_lvl = int(resources["milk"])
    coffee_lvl = int(resources["coffee"])

    for coin in coins_amount:
        money_lvl += float(coins_amount[coin][0] * coins_amount[coin][1])
    return water_lvl, milk_lvl, coffee_lvl, money_lvl

resource_lvl = [report()[0], report()[1], report()[2], report()[3]]
#Once the coffee is ordered, add all the ingredient levels of the ordered coffee here
def coffee_machine():
    global resource_lvl
    # Clear coffee_ordered list, and coins/money_lvl
    coffee_ordered = []



    order_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
# TODO: Add report as an option to print a report on the amount of resources left
    if order_coffee == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resource_lvl[3]}")
        coffee_machine()
        return resource_lvl
# TODO: If the user asks for a coffee, check the resource levels
    elif order_coffee == "espresso" or order_coffee == "latte" or order_coffee == "cappuccino":
        # Iterate through the ordered ingredients and add them to the empty list
        while len(coffee_ordered) < 2:
            # Iterate through the resources dictionary and subtract the resources in the coffee_ordered list
            # If the subtracted value is less than 0, Print there's not enough and start the function again
                for taken in resources:
                    coffee_ordered.append(MENU[order_coffee]["ingredients"][taken])
                    # resource_taken = float(resources[taken] - MENU[order_coffee]["ingredients"][taken])
                    resources[taken] -= MENU[order_coffee]["ingredients"][taken]
                    if resources[taken] < 0:
                        print(f"Sorry there is not enough {taken}. Money refunded")
                        coffee_machine()


# TODO: If there's enough resources, ask for quarters/dimes/nickles/pennies
        print("Please insert coins.")
        # Iterate through coins_amount and ask how many of each coin is being deposited
        for deposit in coins_amount:
            depo_ask = float(input(f"How many {deposit}?: "))
        # Add the amount of deposits to the second part of the array
            coins_amount[deposit][1] += depo_ask
        # Multiply the amount of coins deposited by the coins amounts and add the sum to the money_lvl
            coin_cost = coins_amount[deposit][0] * coins_amount[deposit][1]
            resource_lvl[3] += coin_cost
# TODO: If the money is enough, deposit the drink and tell them to enjoy.
        if resource_lvl[3] == MENU[order_coffee]["cost"]:
            print(f"Here is your {order_coffee}  Enjoy!")
            clear()
# If it's too much, give them change, deposit drink
        elif resource_lvl[3] > MENU[order_coffee]["cost"]:
            change_diff = float(resource_lvl[3] - MENU[order_coffee]["cost"])
            print(f"Here is ${change_diff} in change.")
            print(f"Here is your {order_coffee}  Enjoy!")
            clear()
# If it's too little, "Sorry not enough"
        elif resource_lvl[3] < MENU[order_coffee]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            clear()
        else:
            print("Invalid number entered. Try again.")
            coffee_machine()
            clear()
# TODO:  Clear the coffee_ordered list, clear coins_amounts, and restart function (at the top)
    else:
        # Invalid check and restart the function
        print("That's not a valid item or receipt number. Try again.")
        coffee_machine()

def clear():
    for clears in coins_amount:
        coins_amount[clears][1] = 0

    resource_lvl[3] = 0

    coffee_machine()


coffee_machine()