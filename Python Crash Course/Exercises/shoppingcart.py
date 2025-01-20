item = input('What item would you like to buy?: ')
price = float(input('How much does it cost?: '))
quantity = int(input('How many would you like to buy?: '))
total = price * quantity

print(f'You are buying {quantity} {item} at {price} each for a total of {total}')