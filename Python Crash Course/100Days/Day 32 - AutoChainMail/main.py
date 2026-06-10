##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib
import random
import glob

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
curr_day = now.day
curr_month = now.month

g_email = "spacecadet049@gmail.com"
h_email = "automatic_senda@hotmail.com"

password = "eioj cjuh zovr tujg"

birth_cal = pd.read_csv("birthdays.csv")
birth_row = birth_cal[(birth_cal["month"] == curr_month) & (birth_cal["day"] == curr_day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if not birth_row.empty:
    for index, row in birth_row.iterrows():
        letter_temps = glob.glob("letter_templates/*.txt")
        random_letter= random.choice(letter_temps)
        birth_name = row["name"]
        birth_email = row["email"]

        with open(random_letter) as file:
            letter_words = file.read().replace("[NAME]", birth_name)

        with  smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=g_email, password=password)
            connection.sendmail(
                from_addr=g_email,
                to_addrs=h_email,
                msg=f"Subject:Happy Birthday {birth_name}!\n\n{letter_words}"
            )

# 4. Send the letter generated in step 3 to that person's email address




