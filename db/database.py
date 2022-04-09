import sqlite3

class Cache:
    def __init__(self):
        conn = sqlite3.connect('cache.sqlite')
        conn.execute('CREATE TABLE IF NOT EXISTS Temperatures (city TEXT, country TEXT, max REAL, min REAL)')
    
    def get_cached_temperatures(self, city, max_entries):
        conn.execute('SELECT FROM Temperatures WHERE ')

    