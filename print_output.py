from datetime import datetime
import calendar

def print_current_weather(in_dict):
    city = in_dict['location']['name']
    state = in_dict['location']['region']
    temp = in_dict['current']['temp_f']
    wind_mph = in_dict['current']['wind_mph']
    wind_dir = in_dict['current']['wind_dir']

    print(f"\nThe current temperature in {city}, {state} is {temp}F with {wind_mph} winds out of the {wind_dir}")


def print_forecast(in_dict):
    #print(in_dict)
    for x in in_dict['forecast'].get('forecastday'):
        day_of_week = calendar.day_name[datetime.strptime(x['date'], '%Y-%m-%d').weekday()]
        high = x['day']['maxtemp_f']
        low = x['day']['mintemp_f']

        print(f"{day_of_week}'s high will be {high}F with a low of {low}F")


