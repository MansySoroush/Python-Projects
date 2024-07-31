import requests
import datetime as dt
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Find your API Keys at following Urls
# and set them as environment variables.

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "XXXX"
NEWS_API_KEY = "YYYY"

TW_ACCOUNT_SID = "ZZZZ"
TW_AUTH_TOKEN = "TTTT"

tesla_price_increased = True


def get_tesla_stock_price_diff_percent():
    # STEP 1: Use https://www.alphavantage.co/documentation/#daily
    # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    # TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
    # e.g. [new_value for (key, value) in dictionary.items()]

    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "interval": "60min",
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
    response.raise_for_status()
    data = response.json()

    today = dt.datetime.now()
    yesterday = today - dt.timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")

    yesterday_close_price = float(data["Time Series (Daily)"][yesterday_date]["4. close"])

    print(yesterday_close_price)

    # TODO 2. - Get the day before yesterday's closing stock price
    before_yesterday = today - dt.timedelta(days=2)
    before_yesterday_date = before_yesterday.strftime("%Y-%m-%d")

    before_yesterday_close_price = float(data["Time Series (Daily)"][before_yesterday_date]["4. close"])

    # print(data["Time Series (Daily)"][before_yesterday_date]["4. close"])
    print(before_yesterday_close_price)

    # TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
    # Hint: https://www.w3schools.com/python/ref_func_abs.asp
    global tesla_price_increased
    tesla_price_increased = True if yesterday_close_price > before_yesterday_close_price else False

    diff = round(abs(yesterday_close_price - before_yesterday_close_price), 2)
    print(diff)

    # TODO 4. - Work out the percentage difference in price between closing price yesterday and
    # closing price the day before yesterday.
    percentage = round((diff / before_yesterday_close_price) * 100, 2)
    print(percentage)

    return percentage


def get_news():
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    today = dt.datetime.now()
    yesterday = today - dt.timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")

    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    data = response.json()

    articles = data["articles"]

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
    #  Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    return three_articles


def send_article_via_sms(title, description, percentage):
    if title is None:
        title = ""

    if description is None:
        description = ""

    # Optional TODO: Format the message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
    special_char = "🔺" if tesla_price_increased else "🔻"

    client = Client(TW_ACCOUNT_SID, TW_AUTH_TOKEN)
    # from_: the phone number that we got from Twilio
    message = client.messages.create(
        body=f"TSLA: {special_char}{percentage}%\nHeadline: {title}\nBrief: {description}",
        from_="+12512990419",
        to="+14372331667")

    print(f"sid: {message.sid}")
    print(f"status: {message.sid}")


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
percent = get_tesla_stock_price_diff_percent()
if percent > 5:
    articles_ = get_news()

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    title_list = [article["title"] for article in articles_]
    desc_list = [article["description"] for article in articles_]
    sms_body_list = [f'Headline: {article["title"]}\nDescription: {article["description"]}' for article in articles_]

    # TODO 9. - Send each article as a separate message via Twilio.
    for i in range(len(articles_)):
        send_article_via_sms(title_list[i], desc_list[i], percent)
