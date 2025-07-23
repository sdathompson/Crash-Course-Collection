from tkinter import *
import random
import string
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_pass():
    password_e.delete(0,len(password_e.get()))

    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()-_=+[]{};:,.<>?")

    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
    remaining = [random.choice(all_chars) for _ in range(9)]

    password_list = [upper, digit, special] + remaining

    password_e.insert(0, ''.join(password_list))
    pyperclip.copy(password_e.get())

    messagebox.showinfo(title="Generated Password!", message="Password copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def google_account():
    is_google = messagebox.askokcancel(title=f"{website_e.get()} with Google", message=f"You used a google account for this profile?")

    if is_google:

        new_data = {
            website_e.get(): {
                "email": email_user_e.get(),
                "password": "Google_Account",
            }
        }

        try:
            with open("data.json", mode="r") as r_data_file:
                # Load data into python dictionary
                data = json.load(r_data_file)
                # Update the data into the structure
                data.update(new_data)

        except FileNotFoundError as f_error:
            messagebox.showwarning(title="No JSON file found.",
                                   message=f"{str(f_error)}. Creating JSON file...\nYou must add the account again.")
            with open("data.json", mode="w") as create_json:
                create_json.write("{}")
        else:
            if len(website_e.get()) == 0:
                messagebox.showerror(title="No Web Name", message="You must provide a website name before you initialize a google account")
            else:
                with open("data.json", mode="w") as w_data_file:
                    # Saving updated data
                    json.dump(data, w_data_file, indent=4)
        finally:
            website_e.delete(0, len(website_e.get()))
            password_e.delete(0, len(website_e.get()))
            website_e.focus()

def fields_entry():
    contains_digit = any(char in string.digits for char in password_e.get())
    contains_special = any(char in "!@#$%^&*()-_=+[]{};:,.<>?"  for char in password_e.get())
    contains_letters = any(char in string.ascii_letters for char in password_e.get())

    new_data = {
        website_e.get(): {
            "email": email_user_e.get(),
            "password": password_e.get(),
        }
    }

    is_ok = messagebox.askokcancel(title=website_e.get(), message=f"Do you want to save this profile?: \nEmail/User: {email_user_e.get()}\nPassword: {password_e.get()}" )

    if is_ok:
        if len(password_e.get()) < 4 or not contains_digit or not contains_special or not contains_letters:
            messagebox.showerror("Invalid Password ", "Password length must be at least 4 characters long and contain at least one special character, uppercase character, and number")
        elif len(website_e.get()) == 0 or len(password_e.get()) == 0:
            messagebox.showerror(title="Fields Empty", message="Please make sure you haven't left any fields empty.")
        else:
            # Try to read the .json and write to it
            try:
                with open("data.json", mode="r") as r_data_file:
                    # Load data into python dictionary
                    data = json.load(r_data_file)
                    # Update the data into the structure
                    data.update(new_data)

            except FileNotFoundError as f_error:
                messagebox.showwarning(title="No JSON file found.", message=f"{str(f_error)}. Creating JSON file...\nYou must add the account again.")
                with open("data.json", mode="w") as create_json:
                    create_json.write("{}")
            else:
                with open("data.json", mode="w") as w_data_file:
                    # Saving updated data
                    json.dump(data, w_data_file, indent=4)
            finally:
                    website_e.delete(0, len(website_e.get()))
                    password_e.delete(0, len(password_e.get()))
                    website_e.focus()



# ----------------------------- SEARCH ---------------------------------- #
def search_entries():
    search_query = website_e.get()
    # try:
    # Get the json data into a dictionary (json.load)
    with open("data.json", mode="r") as data_file:
        search_data = json.load(data_file)
# Iterate through the dictionary to search all the website names.
        for websites in search_data:
# If website name is equal to the string in the website entry box
# return the Email/Username and Password in a messagebox
            if search_query == websites:
                messagebox.showinfo(title=search_query, message=f"Email: {search_data[websites]["email"]}\nPassword: {search_data[websites]["password"]}")
            else:
                messagebox.showwarning(title="Invalid Website", message="Entry does not exist")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
lock_img = PhotoImage(file="logo.png")

# Canvas and Lock Image
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website Label
website = Label(text="Website:", justify="center", padx=5)
website.grid(column=0, row=1)

website_e = Entry(width=33)
website_e.grid(column=1, row=1, sticky="w")
website_e.focus()

# Email/Username
email_user = Label(text="Email/Username:", justify="center", padx=5)
email_user.grid(column=0, row=2)

email_user_e = Entry(width=54)
email_user_e.grid(column=1, row=2, columnspan=2, sticky="w")
email_user_e.insert(0, "shanedathompson@gmail.com")

# Password
password = Label(text="Password:", justify="center", padx=5)
password.grid(column=0, row=3)

password_e = Entry(width=33)
password_e.grid(column=1, row=3, sticky="w")

gen_pass = Button(text="Generate Password", width=16, command=random_pass)
gen_pass.grid(column=2, row=3, sticky="w")

add_pass = Button(text="Add", width=45, command=fields_entry)
add_pass.grid(column=1, row=4, columnspan=2, sticky="w")

add_google_account = Button(text="Add a google account", width=45, command=google_account)
add_google_account.grid(column=1, row=5, columnspan=2, sticky="w")

# Search
search = Button(text="Search", width=16, command=search_entries)
search.grid(column=2, row=1)



window.mainloop()