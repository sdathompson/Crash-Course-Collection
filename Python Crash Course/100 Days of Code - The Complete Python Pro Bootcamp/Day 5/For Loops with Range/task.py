def gauss_challenge():
    gauss_sum = 0

    for number in range(1, 101):
        gauss_sum += number

    print(gauss_sum)

def fizzbuzz():
    for number in range(1, 101):

        if number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 and 5:
            print("FizzBuzz")
        else:
            print(number)
