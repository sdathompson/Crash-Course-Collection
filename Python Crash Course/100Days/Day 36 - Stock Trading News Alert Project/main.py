# TODO: 1. Grab some stock data for today and the previous day. Get the difference between the two prices in a flat value and a percentage. Also get the direction it went (up or down?)
# TODO: 2. Get some news for the stock if the tracked stock rose or fell by a certain percentage.
# TODO: 3. Send ourselves an SMS/email that contains: the big drop that happened.
import os
from dotenv import load_dotenv
from pyexpat.errors import messages
from api import ApiCall
from sender import SmtpEmails
from datetime import date, timedelta
from twilio.rest import Client

load_dotenv()

ALPHA_KEY = str(os.environ.get("ALPHA_KEY"))
news_key = str(os.environ.get("NEWS_KEY"))
twilio_sid = str(os.environ.get("TWILIO_SID"))
twilio_token = str(os.environ.get("TWILIO_TOKEN"))
TWILIO_VIR_NUM = str(os.environ.get("VIR_NUM"))
MY_PHONE_NUMBER = str(os.environ.get("MY_PHONE"))
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

p_daily = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": ALPHA_KEY,
}

news_daily = {
    "q" : COMPANY_NAME,
    "apikey" : news_key,
}

today_date = date.today()
yesterday_date = date.today() - timedelta(days=1)

price_today = ApiCall(end="https://www.alphavantage.co/query", para=p_daily).api_req()["Time Series (Daily)"][f"{today_date}"]['4. close']
price_yesterday = ApiCall(end="https://www.alphavantage.co/query", para=p_daily).api_req()["Time Series (Daily)"][f"{yesterday_date}"]['4. close']

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
news_get = ApiCall(end="https://newsapi.org/v2/everything", para=news_daily).api_req()['articles']

if abs(float(price_today) - float(price_yesterday)) >= float(price_yesterday) * 0.05:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    three_articles = news_get[:3]
    print(three_articles)

    formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(twilio_sid, twilio_token)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_=TWILIO_VIR_NUM,
            to=MY_PHONE_NUMBER,
        )

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

