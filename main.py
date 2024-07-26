from weather import get_current_weather_by_zip, get_forecast_weather_by_zip, InvalidZip
from print_output import print_current_weather, print_forecast

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

print("Welcome to the weather app\n")
search_zip = input("\nWhat zip code would you like the weather for: ")
weather_option = input("\nWould you like current or forecast [C/F]: ")

try:
    if weather_option.lower() == "c":
        current_weather = get_current_weather_by_zip(api_key, search_zip)
        print_current_weather(current_weather)

    else:
        forecast = get_forecast_weather_by_zip(api_key, search_zip)
        print_forecast(forecast)

except InvalidZip:
    print("Bad zip")

