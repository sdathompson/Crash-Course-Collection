# TODO-1: Import and print the logo from art.py when the program starts.
from contextlib import nullcontext


from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input:
            return user_input
        print("Invalid entry. Please try again. \n")

should_continue = True

while should_continue:

    direction = get_valid_input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid entry")
        continue
    text = get_valid_input("Type your message:\n").lower()
    if text is None:
        print("Invalid entry")
        continue
    shift = get_valid_input("Type the shift number:\n")
    if shift.isdigit():
        shift = int(shift)
    else:
        print("Invalid entry")
        continue


    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    ask = input("\nDo you want to continue? 'Y' for yes and 'N' for no:\n").lower()

    if ask == 'n':
        should_continue = False
        print("Goodbye")




