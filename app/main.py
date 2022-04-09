import os
import requests

from datetime import datetime
from flask import Flask, request
from dotenv import load_dotenv
from db.database import Cache

env = load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

@app.get('/temperature/<city_name>')
def get_temperature(city_name):
    cache = Cache()

    parameter = request.args.get('max')
    if parameter:
        cache_list = cache.get_cached_temperatures(city_name, parameter)
        return {'data': cache_list }

    last_cache = cache.get_cached_temperatures(city_name, 1)
    if last_cache:
        (name, country, max_t, min_t, str_date) = last_cache[0]
        
        date = datetime.strptime(str_date[:19], '%Y-%m-%d %H:%M:%S')
        if (date - datetime.now()).seconds < 900:
            return { 'name': name, 'country': country, 'max': max_t, 'min': min_t, 'avg': float(format((max_t+min_t)/2, '.2f')) }

    url_geocoding_api = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}'
    place = requests.get(url_geocoding_api).json()
    lat, lon = (place[0]['lat'], place[0]['lon'])

    url_temperature_api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    data = requests.get(url_temperature_api).json()

    avg = float(format((data['main']['temp_min'] + data['main']['temp_max'])/2, '.2f'))

    data = {
        'name': data['name'], 
        'country': data['sys']['country'],  
        'min': data['main']['temp_min'], 
        'max': data['main']['temp_max'], 
        'avg': avg
    }

    cache.create_cache_entry(data['name'], data['country'], data['max'], data['min'])

    return data
