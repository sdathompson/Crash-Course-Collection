# Quiz question: filter products under $20

products = [
    { "name": "Book", "price": 15 },
    { "name": "Lamp", "price": 30 },
    { "name": "Pen", "price": 5 }
]
def filter_prod():
    for product in products:
        if product["price"] < 20:
            print(product["price"])

filter_prod()
