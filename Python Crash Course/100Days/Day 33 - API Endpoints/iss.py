import requests
from datetime import datetime
import time
from APi import ApiCall as aPI
from sender import SmtpEmails as sEND

MY_LAT = 43.898750
MY_LNG = -79.448396
parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted": 0,
}

iss_email = sEND()
iss_api = aPI(end="http://api.open-notify.org/iss-now.json")
sun_api = aPI(end="https://api.sunrise-sunset.org/json", para=parameters)

iss_data = iss_api.api_req()

#ISS Lat + Long
iss_lat = float(iss_data["iss_position"]["latitude"])
iss_lng = float(iss_data["iss_position"]["longitude"])

sun_data = sun_api.api_req()

# Sunrise + Sunset HR
sunrise_hr = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hr = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

# Current Time
time_now_hr = datetime.now().hour

# If the ISS is close ot my current position
# and it is currently dark
while True:
    if abs(MY_LAT - iss_lat) < 5 and abs(MY_LNG - iss_lng) < 5 and time_now_hr > 7:
    # Then send me an email to look up
        iss_email.send_gmail(
            from_email=iss_email.g_email,
            to_email=iss_email.h_email,
            msg_email="Subject:ISS is near!\n\nThe ISS is somewhere above you tonight. Remember to look up! :)")
    else:
        print("The ISS is off on another journey")
# BONUS: run the code every 60 seconds
    time.sleep(60)
