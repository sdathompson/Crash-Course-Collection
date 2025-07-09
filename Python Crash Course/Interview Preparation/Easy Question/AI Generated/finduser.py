# Quiz question: find the user named Jess
users = [
    { "name": "Sam", "age": 25 },
    { "name": "Jess", "age": 30 },
    { "name": "Lee", "age": 22 }
]

for user in users:
    if user["name"] == "Jess":
        print(user["name"])