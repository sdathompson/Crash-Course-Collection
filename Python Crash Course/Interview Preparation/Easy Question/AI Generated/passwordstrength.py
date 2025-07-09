# Check if a password is strong:
# at least 8 characters, contains a number, and a capital letter.

passwords = [
    "simple123",
    "StrongPass1",
    "weak",
    "CapButNoNum",
    "12345678"
]

def is_password_strong(password):
    valid = []
    one_digit = 0
    one_letter = 0
    for my_pass in passwords:
        if (len(my_pass) >= 8
                and sum(char.isdigit() for char in my_pass) >= 1
                and sum(char.isupper() for char in my_pass) >= 1):
            valid.append(True)
        else:
            valid.append(False)
    return valid


print(is_password_strong(passwords))

