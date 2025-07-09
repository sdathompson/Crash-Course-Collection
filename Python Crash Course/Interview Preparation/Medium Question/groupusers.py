# Group users by role
# Output = {"admin": ["Alice","Charlie"], "user":["Bob","Dana"]}

def roles_to_users(user):
    allocation = dict()
    for entry in user:
        role = entry["role"]
        user = entry["name"]
        if role not in allocation:
            allocation[role] = []
        allocation[role].append(user)
    return print(allocation)



roles_to_users([
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "Dana", "role": "user"}
])
