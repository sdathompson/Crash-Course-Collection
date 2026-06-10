# import smtplib
# # spacecadet049@gmail.com - automatic_senda@hotmail.com
# # Gmail connection - smtp.gmail.com
# # Hotmail connection - smtp.live.com
# # Yahoo connection - smtp.mail.yahoo.com
#
#
# # Remember to pick a port
# with  smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     # Secure the connection with starttls()
#     connection.starttls()
#     # Login
#     connection.login(user=g_email, password=password)
#     connection.sendmail(
#         from_addr=g_email,
#         to_addrs=h_email,
#         msg="Subject:Hello\n\nThis is the body of the e-mail")

# import datetime as dt
# from calendar import weekday
#
# # Print current date and time with a high degree of accuracy
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# week_day = now.weekday()

g_email = "spacecadet049@gmail.com"
h_email = "automatic_senda@hotmail.com"

password = "eioj cjuh zovr tujg"

import smtplib
import datetime as dt
import random
#TODO: 1. Use the datetime module to acquire the current day of the week.
now = dt.datetime.now()
day_of_week = now.weekday()
#TODO: 2. Open the quotes.txt file and obtain a list of quotes
def random_quote_gen():
    with open("quotes.txt") as file:
        quotes = file.readlines()
#TODO: 3. Use the random module to pick a random quote from your list of quotes
    random_q_choice = random.choice(quotes)
    return random_q_choice
print (day_of_week)
#TODO: 4. Use the smtplib to send the email to yourself
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=g_email, password=password)
    if day_of_week == 0:
        connection.sendmail(
            from_addr=g_email,
            to_addrs=h_email,
            msg=f"Subject:Motivational Quote of the Day\n\n{random_quote_gen()}"
        )
    else:
        connection.sendmail(
            from_addr=g_email,
            to_addrs=h_email,
            msg="Subject: No Motivation Quote Today\n\n Keep going throughout the week. You got it :)"
        )