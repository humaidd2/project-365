import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = ""
NEWS_API_KEY = ""

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "datatype": "json",
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)

time_data = response.json()["Time Series (Daily)"]
data = [value for (key, value) in time_data.items()]

y_closing = data[0]["4. close"]
dy_closing = data[1]["4. close"]

diff = (abs(float(dy_closing) - float(y_closing)) / float(dy_closing)) * 100

parameters_news = {
    "q": STOCK_NAME,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY

}

if diff > 1:
    news_respone = requests.get(NEWS_ENDPOINT, params=parameters_news)
    a = news_respone.json()["articles"]
    for i in a[:3]:
        title = i["title"]
        brief = i["description"]

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'TSLA:\n Headline: {title} \n Brief: {brief}',
            from_='+14847598097',
            to='+201050071610'
        )
