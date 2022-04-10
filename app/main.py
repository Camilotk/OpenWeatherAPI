import os
import requests

from datetime import datetime
from flask import Flask, request
from dotenv import load_dotenv
from db.database import Cache

env = load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

def calc_average_temperature(max, min):
    return float(format((max + min)/2, '.2f'))

def cache_is_valid(date):
    TIME_LIMIT = int(os.getenv('MAX_TIME_LIMIT_SECONDS'))
    time_in_seconds = (date - datetime.now()).total_seconds()
    return time_in_seconds < TIME_LIMIT

def return_if_cache_is_valid(cache):
    (name, country, max_temp, min_temp, str_date) = cache[0]
    cache_date = datetime.strptime(str_date[:19], '%Y-%m-%d %H:%M:%S')
    data = dict()
    if cache_is_valid(cache_date):
        data = { 
            'name': name, 
            'country': country, 
            'max': max_temp, 
            'min': min_temp, 
            'avg':  calc_average_temperature(max_temp, min_temp) 
        }
    return data

@app.get('/temperature/<city_name>')
def get_temperature(city_name):
    cache = Cache()

    # return the n (n = parameter) entries in cache
    parameter = request.args.get('max')
    if parameter:
        cache_list = cache.get_cached_temperatures(city_name, parameter)
        return {'data': cache_list }

    # check if cache exists and returns it before check API
    last_cache = cache.get_cached_temperatures(city_name, 1)
    if last_cache:
        cache_data = return_if_cache_is_valid(last_cache)
        if cache_data:
            return cache_data
    
    # makes the API request
    url_geocoding_api = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}'
    place = requests.get(url_geocoding_api).json()
    lat, lon = (place[0]['lat'], place[0]['lon'])

    url_temperature_api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    data = requests.get(url_temperature_api).json()

    avg_temp = calc_average_temperature(data['main']['temp_max'], data['main']['temp_min'])
  
    # muounts the return
    data = {
        'name': data['name'], 
        'country': data['sys']['country'],  
        'min': data['main']['temp_min'], 
        'max': data['main']['temp_max'], 
        'avg': avg_temp
    }

    # cache 
    cache.create_cache_entry(data['name'], data['country'], data['max'], data['min'])

    return data
