import os
import requests
from dotenv import load_dotenv

import pandas as pd

# import API_KEY from .env

load_dotenv()
API_KEY = os.getenv("API_KEY")

# openweather url
# base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API_KEY}"
base_url = f"https://api.openweathermap.org/data/2.5/weather"

print(base_url)

def extract_data(city: str) -> dict:
    print("extract_data is running.")
    url = f"{base_url}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    # print(response.json())
    return response.json()

# print("extract_data('Mumbai')", type(extract_data('Mumbai')), extract_data('Mumbai'))

def transform_data(data: dict) -> dict:
    print("transform_data is running.")
    transformed_data = {
        "city": data['name'],
        "latitude": data['coord']['lat'],
        "longitude": data['coord']['lon'],
        "temp": data['main']['temp'],
        "description": data['weather'][0]['description']
    }

    return transformed_data

# data = extract_data('Mumbai')
# print("transform_data(data)", type(transform_data(data)), transform_data(data))


def load_data(data: dict, filename: str) -> None:
    print("load_data is running.")
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)

# load_data(data)

def run_etl_pipeline(city: str) -> None:
    extracted_data = extract_data(city)
    transformed_data = transform_data(extracted_data)
    load_data(transformed_data, f'weather_data_{city}.csv')

city = 'Mumbai'
run_etl_pipeline(city)