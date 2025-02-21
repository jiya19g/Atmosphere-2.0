import time
from locust import HttpUser, task, between

API_KEY = "13e5b9ac55449dded8d96c84b478dfa6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

class WeatherAPITest(HttpUser):
    wait_time = between(2, 5)  # Wait 2-5 seconds between requests to avoid rate limits

    @task
    def test_weather_api(self):
        self.make_request("London")

    @task
    def test_invalid_city(self):
        self.make_request("InvalidCity")

    def make_request(self, city):
        retry_delay = 1  # Start with 1 sec delay for retrying

        while True:
            response = self.client.get(f"{BASE_URL}?q={city}&appid={API_KEY}")
            
            if response.status_code == 200:
                print(f"Success: {city}")
                break  # Exit loop on success

            elif response.status_code == 429:  # Too Many Requests
                print(f"Rate limit hit! Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff (1s → 2s → 4s → 8s)
                
                if retry_delay > 30:  # Max wait time = 30 sec
                    print("API rate limit exceeded. Stopping request.")
                    break

            else:
                print(f"API Error ({response.status_code}) for {city}")
                break  # Stop retrying on non-rate-limit errors
