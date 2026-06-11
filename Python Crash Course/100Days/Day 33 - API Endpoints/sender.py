import smtplib

class SmtpEmails:
    def __init__(self):
        self.g_email = "spacecadet049@gmail.com"
        self.h_email = "automatic_senda@hotmail.com"
        self.g_app_pass = "eioj cjuh zovr tujg"

    def send_gmail(self, from_email, to_email, msg_email):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.g_email, password=self.g_app_pass)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_email,
                msg=msg_email
            )