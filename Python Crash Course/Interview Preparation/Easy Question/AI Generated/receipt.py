# Format a list of purchases
# into a neat receipt string

# Output -
# Book - $12.99
# Pen - $1.99
# Lamp - $22.50
# Total: $37.48

def receipt(purchases):
    for buy in purchases:
        print(f"{buy["item"]} - ${buy["price"]}\n")
    return purchases

receipt(purchases = [
    { "item": "Book", "price": 12.99 },
    { "item": "Pen", "price": 1.99 },
    { "item": "Lamp", "price": 22.50 }
])

