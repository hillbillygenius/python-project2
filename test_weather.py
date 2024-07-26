import pytest
import json
import requests
from unittest.mock import patch, Mock 
from weather import get_current_weather_by_zip, InvalidZip

import os
from dotenv import load_dotenv

@patch('weather.requests.get')
def test_get_weather_sucess_mock(mock_get):
    api_key = "valid_api_key"
    
    expected_response = {
        "temp_f":80, 
        "wind_mph": 10.2,
        "wind_dir": "N"
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = expected_response

    response = get_current_weather_by_zip(api_key,61754)
    assert response == expected_response

@patch('weather.requests.get')
def test_get_weather_http_error_mock(mock_get):
     
     api_key = "invalid_api_key"

     #with patch('weather.requests.get') as mock_get:
     mock_get.return_value.status_code = 403
     mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

     response = get_current_weather_by_zip(api_key, 61754)
     assert "HTTP error occurred" in response

def test_get_weather_bad_zip():
    load_dotenv()

    api_key = os.getenv("WEATHER_API_KEY")
    
    with pytest.raises(InvalidZip):
        get_current_weather_by_zip(api_key,'aaaaa')
    
# def test_get_weather_success():
#     load_dotenv()

#     api_key = os.getenv("WEATHER_API_KEY")
    
#     response = get_current_weather_by_zip(api_key,61754)
#     assert response['location']['name'] == 'Mc Lean' 

# def test_get_weather_http_error():
#     api_key = 'bad key'

#     response = get_current_weather_by_zip(api_key,61754)
#     assert "HTTP error occurred" in response      