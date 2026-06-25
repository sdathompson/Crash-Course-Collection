import smtplib
import os

class SmtpEmails:
    def __init__(self):
        self.g_email = os.environ.get("g_email")
        self.h_email = os.environ.get("h_email")
        self.g_app_pass = os.environ.get("g_app_pass")
        self.port_num = int(os.environ.get("port_num"))

    def send_gmail(self, from_email, to_email, msg_email):
        with smtplib.SMTP("smtp.gmail.com", self.port_num) as connection:
            connection.starttls()
            connection.login(user=self.g_email, password=self.g_app_pass)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_email,
                msg=msg_email,
            )