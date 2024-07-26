import pytest
import json
from print_output import print_current_weather,print_forecast

from pathlib import Path

#stdout


def test_print_current_weather(capfd):
    in_dict = {}
    p = Path(__file__).with_name('current.json')
    with p.open('r') as f:
        in_dict = json.load(f)
    
    print_current_weather(in_dict)
    out, err = capfd.readouterr()
    assert out == "\nThe current temperature in Mc Lean, Illinois is 75.0F with 6.5 winds out of the E\n"
    



def test_print_forecast(capfd):
    in_dict = {}
    p = Path(__file__).with_name('forecast.json')
    with p.open('r') as f:
        in_dict = json.load(f)
    
    print_forecast(in_dict)
    out, err = capfd.readouterr()
    assert out == "Friday's high will be 77.0F with a low of 56.9F\nSaturday's high will be 79.0F with a low of 60.2F\nSunday's high will be 79.7F with a low of 68.2F\nMonday's high will be 81.2F with a low of 65.7F\nTuesday's high will be 86.1F with a low of 70.4F\n"
    

