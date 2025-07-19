# Unlimited OPTIONAL Arguments  - def function(*[attributes])

def add(*args):
    add_ptr = 0
    result = 0

    while add_ptr < len(args) - 2:
        result = sum(args)
        add_ptr += 1
    return result


add(1, 2, 4, 5, 7, 8, 7, 2, 2, 6, 8, 8, 9)

# Unlimited OPTIONAL Keyword Arguments - def function(**[attributes])

def calculate(n, **kwargs):
    #dictionary = {kwarg:value}
    for key, value in kwargs.items():
        print(key, value)

    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)

# You can set all of the options or you can leave them as their default values

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.make)