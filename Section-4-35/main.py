import requests
from email.message import EmailMessage
import ssl
import smtplib
import os

# NOTE-TO-SELF: Use environment variables before publishing.

param = {
    "appid": os.environ["MY_APPID"],
    "lat": -23.444370,
    "lon": -46.919079,
    "units": "metric"}

url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=url, params=param)
response.raise_for_status()
data = response.json()
will_rain = False
i = 0


while i < 7:
    condition_code = data["list"][i]["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    i += 1

if will_rain:

    email_sender = os.environ["MY_BOT_EMAIL"]
    my_password = os.environ["MY_BOT_PASSWORD"]
    email_receiver = os.environ["MY_EMAIL"]

    subject = "Lá vem chuva!"
    body = "Leve um guarda-chuva hoje."

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, my_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
