# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# # print(total_words)


def fizz_buzz(target):
    for number in range(1, (target + 1)):
        if number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        else:
            print(number)

print(fizz_buzz(15))