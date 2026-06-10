import os
import requests
from dotenv import load_dotenv

import pandas as pd
from datetime import date, datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")

base_url = f"https://api.openweathermap.org/data/2.5/weather"
# print(base_url)

def extract_data(city: str) -> dict:
    url = f"{base_url}?q={city}&appid={API_KEY}"
    response = requests.get(url)

    print("extract_data func has completed.")
    # print(response.json())
    return response.json()

# print("extract_data('Mumbai')", type(extract_data('Mumbai')), extract_data('Mumbai'))

def transform_data(data: dict) -> dict:
    global timestamp_converted
    _now = datetime.now()
    timestamp = _now.strftime("%Y-%m-%d %H:%M:%S")
    timestamp_converted = _now.strftime("%d%m%Y_%H%M%S")

    transformed_data = {
        "city": data['name'],
        "timestamp": timestamp,
        "latitude": data['coord']['lat'],
        "longitude": data['coord']['lon'],
        "temp": data['main']['temp'],
        "description": data['weather'][0]['description']
    }

    print("transform_data func has completed.")
    return transformed_data     #, timestamp

# data = extract_data('Mumbai')
# print("transform_data(data)", type(transform_data(data)), transform_data(data))


def load_data(data: dict) -> None:
    df = pd.DataFrame([data])
    filename = f'weather_data_{city}_{timestamp_converted}.csv'
    df.to_csv(filename, index=False)
    print(filename)
    print("load_data func has completed.")
# load_data(data)

def run_etl_pipeline(city: str) -> None:
    
    try:
        extracted_data = extract_data(city)
        transformed_data = transform_data(extracted_data)
        # load_data(transformed_data, f'weather_data_{city}_{timestamp_converted}.csv')
        load_data(transformed_data)
    
        print(f'File weather_data_{city}_{timestamp_converted}.csv created.')

    # except ConnectionError as e:
    except requests.exceptions.ConnectionError as e:
        # print(e.__str__)
        print("No internet connection")
    
city = 'Mumbai'
run_etl_pipeline(city)