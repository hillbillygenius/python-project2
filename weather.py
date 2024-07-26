import requests

class InvalidZip(Exception):
    pass

def get_current_weather_by_zip(api_key, zip):
    if str(zip).isdigit():

        API_URL = "http://api.weatherapi.com/v1/current.json"

        params = {
            "key": api_key
            ,"q": zip
            ,"aqi": "no"

        }

        try:
            response = requests.get(API_URL,params = params)
            response.raise_for_status()
            weather_data = response.json()
            return weather_data
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"
    
    else:
        raise InvalidZip("Zip must be numeric")
    
def get_forecast_weather_by_zip(api_key, zip):
    if str(zip).isdigit():

        API_URL = "http://api.weatherapi.com/v1/forecast.json"

        params = {
            "key": api_key
            ,"q": zip
            ,"days": "5"
            ,"aqi": "no"
            ,"alerts":"no"
        }

        try:
            response = requests.get(API_URL,params = params)
            response.raise_for_status()
            weather_data = response.json()
            return weather_data
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"
    
    else:
        raise InvalidZip("Zip must be numeric")    

