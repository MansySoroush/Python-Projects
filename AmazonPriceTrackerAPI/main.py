from bs4 import BeautifulSoup
import requests
import lxml
from twilio.rest import Client
import smtplib

# Find your ACCOUNT_SID & AUTH_TOKEN at following Url
# and set it as environment variable.
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

TW_ACCOUNT_SID = "XXXX"
TW_AUTH_TOKEN = "YYYY"

YOUR_SMTP_ADDRESS = "..."


def send_email(msg_body):
    my_email = "AAA@gmail.com"

    # An App Password must be added for gmail account and copy it here
    password = "ZZZZ"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=msg_body
        )


def send_sms(msg_body):
    client = Client(TW_ACCOUNT_SID, TW_AUTH_TOKEN)
    # from_: the phone number that we got from Twilio
    message = client.messages.create(
        body=msg_body,
        from_="+11234567890",
        to="+12223334444")

    print(f"sid: {message.sid}")
    print(f"status: {message.sid}")

# https://myhttpheader.com/
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

try:
    span_price_tags = soup.find_all(name="span", class_="a-offscreen")
    if len(span_price_tags) > 0:
        price_text = span_price_tags[0].getText()
        price = float(price_text.split("$")[1])
        print(price)

        if price < 100:
            product_title_tag = soup.find(name="span", id="productTitle")
            product_title = product_title_tag.getText()
            alert_message = f"{product_title} is now {price_text}"

            email_msg = f"Subject:Amazon Price Alert!\n\n{alert_message}\n{URL}".encode("utf-8")
            sms_msg = f"Amazon Price Alert!\n\n{alert_message}\n{URL}"

            # send_email(email_msg)
            send_sms(sms_msg)
except:
    print("Error!")
