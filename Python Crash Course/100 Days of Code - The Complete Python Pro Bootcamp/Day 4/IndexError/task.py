def states_list():
    states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                         "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                         "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                         "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                         "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                         "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                         "New Mexico", "Arizona", "Alaska", "Hawaii"]

    print(states_of_america)

def fruits_veg_list():
    # Dirty Dozen fruits and vegetables (2024)
    dirty_dozen = [
        "Strawberries",
        "Spinach",
        "Kale, Collard, and Mustard Greens",
        "Grapes",
        "Peaches",
        "Pears",
        "Nectarines",
        "Apples",
        "Bell and Hot Peppers",
        "Cherries",
        "Blueberries",
        "Green Beans"
    ]
    # Dirty Dozen categorized into fruits and vegetables
    fruits = [
        "Strawberries",
        "Grapes",
        "Peaches",
        "Pears",
        "Nectarines",
        "Apples",
        "Cherries",
        "Blueberries"
    ]

    vegetables = [
        "Spinach",
        "Kale, Collard, and Mustard Greens",
        "Bell and Hot Peppers",
        "Green Beans"
    ]

    dirty_dozen = [fruits, vegetables]
    #Nested list reference
    print(dirty_dozen[1][2])

fruits_veg_list()