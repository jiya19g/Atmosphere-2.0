import requests
import pytest

API_KEY = "13e5b9ac55449dded8d96c84b478dfa6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Test if API returns a successful response for a valid city
def test_valid_city():
    response = requests.get(f"{BASE_URL}?q=London&appid={API_KEY}")
    assert response.status_code == 200
    assert "weather" in response.json()
    
# Test Empty City Name
def test_empty_city():
    response = requests.get(f"{BASE_URL}?q=&appid={API_KEY}")
    assert response.status_code == 400  

# Test Special Characters in City Name
def test_special_characters():
    response = requests.get(f"{BASE_URL}?q=@@@@&appid={API_KEY}")
    assert response.status_code == 404  

# Test API with an invalid city
def test_invalid_city():
    response = requests.get(f"{BASE_URL}?q=InvalidCity&appid={API_KEY}")
    assert response.status_code == 404

# Test API response time
def test_response_time():
    response = requests.get(f"{BASE_URL}?q=New York&appid={API_KEY}")
    assert response.elapsed.total_seconds() < 2  

# Test API structure
def test_response_structure():
    response = requests.get(f"{BASE_URL}?q=Tokyo&appid={API_KEY}")
    json_data = response.json()
    assert "main" in json_data
    assert "wind" in json_data
    assert "weather" in json_data
