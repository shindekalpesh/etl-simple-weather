import os
import requests
from dotenv import load_dotenv

import pandas

# import API_KEY from .env

load_dotenv()
API_KEY = os.getenv("API_KEY")

# openweather url
# base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API_KEY}"
base_url = f"https://api.openweathermap.org/data/2.5/weather"

print(base_url)

def extract_data(city: str) -> dict:
    url = f"{base_url}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    # print(response.url)
    return response.json()

print(extract_data('Mumbai'), type(extract_data('Mumbai')))

def transform_data(data: dict) -> dict:
    pass