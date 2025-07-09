# Return all items from a dictionary that have quantity less than 5
inventory = {
    "apple": 10,
    "banana": 2,
    "orange": 4,
    "grape": 5
}


def inventory_track():
    disc_items = []
    for items in inventory:
        if inventory[items] < 5:
            disc_items.append(items)
    return disc_items

print(inventory_track())



