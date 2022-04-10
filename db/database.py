import sqlite3

from os import remove, path
from datetime import datetime

class Cache:
    def __init__(self, path_name='cache.sqlite'):
        self.conn = sqlite3.connect(path_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Temperatures (city TEXT, country TEXT, max REAL, min REAL, created DATETIME)')
    
    def get_cached_temperatures(self, city, max_entries):
        self.cursor.execute(f'SELECT * FROM Temperatures WHERE city LIKE \'{city}\' ORDER BY created DESC LIMIT {max_entries} COLLATE NOCASE')
        return self.cursor.fetchall()
    
    def create_cache_entry(self, city, country, max_temp, min_temp):
        self.cursor.execute(f'INSERT INTO Temperatures VALUES (\'{city}\', \'{country}\', {max_temp}, {min_temp}, \'{datetime.now()}\');')
        self.conn.commit()
    
    def clear(self):
        remove('cache.sqlite')    