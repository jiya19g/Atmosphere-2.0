import requests
import responses
import pytest

API_KEY = "13e5b9ac55449dded8d96c84b478dfa6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Simulate a 500 Internal Server Error
@responses.activate
def test_mocked_api_failure():
    responses.add(responses.GET, f"{BASE_URL}?q=London&appid={API_KEY}", status=500)

    response = requests.get(f"{BASE_URL}?q=London&appid={API_KEY}")
    assert response.status_code == 500  

# Simulate a 429 Too Many Requests Error
@responses.activate
def test_mocked_rate_limit():
    responses.add(responses.GET, f"{BASE_URL}?q=New York&appid={API_KEY}", status=429)

    response = requests.get(f"{BASE_URL}?q=New York&appid={API_KEY}")
    assert response.status_code == 429  
