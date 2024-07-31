import requests
from twilio.rest import Client
import os

# Singapore
RAINY_LATITUDE = 1.352083
RAINY_LONGITUDE = 103.819839

MY_LOCATION_LATITUDE = 43.938960
MY_LOCATION_LONGITUDE = -79.440780

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# TW_ACCOUNT_SID = "XXXX"
# TW_AUTH_TOKEN = "YYYY"
# OWM_API_KEY = "ZZZZ"

# adding the above keys as Environment Variables
# run command: export OWM_API_KEY=ZZZZ in terminal window

# Get the value of OWM_API_KEY
owm_api_key = os.environ.get("OWM_API_KEY")

# Get the value of TW_AUTH_TOKEN
tw_auth_token = os.environ.get("TW_AUTH_TOKEN")

# Get the value of TW_ACCOUNT_SID
tw_account_sid = os.environ.get("TW_ACCOUNT_SID")


# If you're trying to use Twilio on a PythonAnywhere free account, you're likely to run into an error that looks like this:

# urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.twilio.com', port=443): Max retries exceeded with
# url: /2010-04-01/Accounts/xxxxxx/Messages.json (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection
# object at 0x7fe7acca1630>: Failed to establish a new connection: [Errno 111] Connection refused',))

# The Twilio API client needs to be told how to connect to the proxy server that free accounts use to access the external
# Internet. The code to use to do that differs based on which version of the client library you're using:

# Twilio 6.35.0 onwards:
# -----------------------
# import os
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
#
# proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
#
# account_sid = 'your account id here'
# auth_token = 'your twilio token here'
#
# client = Client(account_sid, auth_token, http_client=proxy_client)
#
# # twilio api calls will now work from behind the proxy:
# message = client.messages.create(to="...", from_='...', body='...')

# Older versions:¶
# -----------------------
# import os
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
#
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#
# account_sid = 'your account id here'
# auth_token = 'your twilio token here'
#
# client = Client(account_sid, auth_token, http_client=proxy_client)
#
# # twilio api calls will now work from behind the proxy:
# message = client.messages.create(to="...", from_='...', body='...')

def send_sms():
    client = Client(tw_account_sid, tw_auth_token)
    # from_: the phone number that we got from Twilio
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+16475436789",
        to="+14376665432")

    print(f"sid: {message.sid}")
    print(f"status: {message.sid}")


def check_weather_to_rain():
    parameters = {
        "lat": MY_LOCATION_LATITUDE,
        "lon": MY_LOCATION_LATITUDE,
        "appid": owm_api_key,
        "cnt": 4,
    }
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()

    will_rain = False
    condition_code_list = [data["list"][i]["weather"][0]["id"] for i in range(0, 4)]
    for code in condition_code_list:
        if code < 700:
            will_rain = True

    print(condition_code_list)
    if will_rain:
        print("Bring an Umbrella!")

    return will_rain
