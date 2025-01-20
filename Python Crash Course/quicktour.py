# # This is my first python program
# print('I like sushi!')

first_name = 'Shane'
food = 'sushi'
email = 'test@test.com'

# # Strings
# print(f'Hello, {first_name}!')
# print (f'You like {food}!')
# print(f'Your email is: {email}!')

# # Integers
age = 27
quantity = 3
num_of_students = 30

# print(f'You are {age} years old!')
# print(f'You buying {quantity} {food}')
# print(f'There are {num_of_students} students in the class')

# Boolean

is_student = True
for_sale = True
is_online = True

# if is_student:
#     print('You are a student')
# else:
#     print('You are not a student')

# if for_sale:
#     print(f'{food} is for sale')
# else:
#     print(f'{food} is not for sale')

# if is_online:
#     print('{name} is online')
# else:
#     print('{name} is offline')

# Python Typecasting
gpa = 3.7


gpa = int(gpa) #output = 3

# Input() prompts the user to return something in the CLI

name = input('What is your name?: ')
# print(f'Hello, {name}!') #output = What's your name?: input , Hello input!

# Math
import math

friends = 0
friends += 1 #output = 1
friends -= 2 #output = -1

abs_friends = abs(friends) #output = 1

pi = 3.14

result = round(pi) #output = 3

result = pow(friends, result) #output = 1^3 = 1

# Conditional Statements - IF

age = int(input('Enter your age: '))

if age >= 18:
    print('What kind of credit card would you like to apply for?')
elif age < 0:
    print('Invalid age')
else:
    print('Not old enough to apply for a credit card')


