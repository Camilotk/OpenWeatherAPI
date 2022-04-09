import os
import requests

from flask import Flask
from dotenv import load_dotenv

env = load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

@app.get('/temperature/<city_name>')
def get_temperature(city_name):
    url_geocoding_api = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}'
    place = requests.get(url_geocoding_api).json()
    lat, lon = (place[0]['lat'], place[0]['lon'])

    url_temperature_api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    data = requests.get(url_temperature_api).json()

    return_data = {
        'min': data['main']['temp_min'],
        'max': data['main']['temp_max'],
        'avg': float(format((data['main']['temp_min'] + data['main']['temp_max'])/2, '.2f')),
        'city': {
            'name': data['name'],
            'country': data['sys']['country']
        }
    }

    return return_data

