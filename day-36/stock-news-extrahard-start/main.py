#!/usr/bin/env python3

import configparser
from os import path
import smtplib
import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AUTH_FILE = f'{path.expanduser("~")}/.keys'
EMAIL = "whendersonii@gmail.com"

config = configparser.RawConfigParser()
config.read(AUTH_FILE)
stock_api_key = config["alpha-vantage"]["key"]
news_api_key = config["news"]["key"]

smtp_email = config["iss"]["email"]
smtp_password = config["iss"]["password"]
smtp_server = config["iss"]["smtp"]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (_, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
if difference > 0:
    title = f"{STOCK}: 📈"
else:
    title = f"{STOCK}: 📉"
difference = abs(difference)
average = (yesterday_closing_price + day_before_yesterday_closing_price) / 2
percentage = (difference / average) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if percentage > 5:
    print("Get News!")

news_params = {
    "q": COMPANY_NAME,
    "qInTitle": COMPANY_NAME,
    "from": "2023-04-28",
    "sortBy": "publishedAt",
    "apiKey": news_api_key,
}

response = requests.get(url=NEWS_ENDPOINT, params=news_params)
articles = response.json()["articles"]
three_articles = articles[:3]

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
formatted_articles = [f"{title}\n" \
                      f"Headline: {article['title']}\n" \
                      f"Brief: {article['description']}\n" \
                      f"Article: {article['url']}"
                      for article in three_articles]

with smtplib.SMTP(smtp_server) as connection:
    connection.starttls()
    connection.login(user=smtp_email, password=smtp_password)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs=EMAIL,
                        msg=f"Subject:Stocks\n\n"
                            f"{formatted_articles[0]}\n\n"
                            f"{formatted_articles[1]}\n\n"
                            f"{formatted_articles[2]}".encode("utf-8"))

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
