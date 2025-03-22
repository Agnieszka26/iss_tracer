import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
GMAIL_HOST_NAME = os.getenv("GMAIL_HOST_NAME")
PORT = int(os.getenv("PORT"))
TIMEOUT= int(os.getenv("TIMEOUT"))
URL_ISS="http://api.open-notify.org/iss-now.json"
URL_SUNRISE = "https://api.sunrise-sunset.org/json"
MY_LAT = 42.2882
MY_LNG = 118.2481

response = requests.get(url=URL_ISS)
response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (float(longitude), float(latitude))
print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url=URL_SUNRISE, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
hour_now = 8
is_dark = hour_now >= int(sunset) or hour_now <= int(sunrise)
iss_lat, iss_lng = iss_position
is_iss_close = (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LNG - 5 <= iss_lng <= MY_LNG + 5)
print(is_dark)
if is_iss_close and is_dark:
    with smtplib.SMTP(GMAIL_HOST_NAME, PORT, timeout=TIMEOUT) as connection:
        connection.starttls()
        connection.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
        connection.sendmail(from_addr=GMAIL_ADDRESS, to_addrs=GMAIL_ADDRESS, msg=f"Subject:Look Up! \n\n"
                                                                                     f"Look in the sky! "
                                                                                 f"There is ISS above your head!")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
