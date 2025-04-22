def my_function():
    for i in range(1, 20):
        i += i
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# The function should print the statement once it reaches 20

# 1. What is the for loop doing?
# It's iterating through the range of 1 to 20

# 2. When is the function meant to print "You got it"?
# It's meant to print when it reaches 20

# 3. What are your assumptions about the value of i?
# the value of i should be increasing as we iterate through the loop and stop when it reaches 20