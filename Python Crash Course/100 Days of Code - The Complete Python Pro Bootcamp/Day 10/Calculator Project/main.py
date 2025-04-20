#TODO: print the logo
import sys
from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
#TODO: Write out the other 3 functions - sub, div, multi.

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

#TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}

#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary


def calculator():
    should_accumulate = True
    n1 = float(input("What's the first number?: "))
    while should_accumulate:

        # Print the operation symbols
        for operation in operations:
            print(operation)
        op = input("Pick an operation: ")

        n2 = float(input("What's the second number?: "))
        answer = operations[op](n1, n2)
        print(f"{n1} {op} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n").lower()
        if choice == "y":
            n1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

#TODO: Ask if the user wants to continue calculating with the result
# or if they want to start a new calculation





