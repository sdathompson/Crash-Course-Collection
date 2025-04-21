# There is no block scope in python

def is_prime(num):
    if num <= 1:
        return False
    for idx in range(2, num):
        if num % idx == 0:
            return False
    return True




print(is_prime(75))