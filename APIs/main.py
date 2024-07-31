# from quote_ui import QuoteUI
#
# quote_ui = QuoteUI()

import WeatherAPI

if WeatherAPI.check_weather_to_rain():
    WeatherAPI.send_sms()


