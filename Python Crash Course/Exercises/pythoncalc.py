# Python calculator

operator = input('Enter operator(+ - * /): ')

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f'{operator} is not a valid operator')

