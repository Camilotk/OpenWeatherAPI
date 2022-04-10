import os
import pytest
import requests

from dotenv import load_dotenv
from db.database import Cache

env = load_dotenv()
BASE_URL = os.getenv('BASE_URL')

@pytest.fixture
def cache_database():
    return Cache()

@pytest.mark.parametrize("city_name", [
    'london',
    'paris',
    'berlin'
])
def test_get_temperature(city_name):
    url = f'{BASE_URL}//temperature/{city_name}'
    response = requests.get(url)
    assert response.status_code == 200