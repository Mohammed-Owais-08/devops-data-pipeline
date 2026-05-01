import requests
import os

API_KEY = os.getenv("API_KEY")

def extract():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()