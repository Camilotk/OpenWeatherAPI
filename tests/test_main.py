import os
import pytest
import requests

from dotenv import load_dotenv
from db.database import Cache
from app.main import return_if_cache_is_valid, calc_average_temperature

env = load_dotenv()
BASE_URL = os.getenv('BASE_URL')

@pytest.fixture
def cache_database():
    return Cache('test.sqlite')

@pytest.mark.parametrize("max, min, expected", [
    (-500, 230, -135.0),
    (456.8,493.7,475.25),
    (-34.7, -80.9, -57.8)
])
def test_calc_average_temperature(max, min, expected):
    avg = calc_average_temperature(max, min)
    assert avg == expected

@pytest.mark.parametrize("city_name", [
    'london',
    'paris',
    'berlin'
])
def test_get_temperature(city_name):
    url = f'{BASE_URL}//temperature/{city_name}'
    response = requests.get(url)
    assert response.status_code == 200

def test_cache_is_valid(cache_database):
    cache_database.create_cache_entry('Bento Gonçalves', 'Brasil', 35.7, 22.3)
    retrieved_cache = cache_database.get_cached_temperatures('Bento Gonçalves', 1)
    response = return_if_cache_is_valid(retrieved_cache)
    assert 'name' in response and 'avg' in response
