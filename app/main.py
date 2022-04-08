from flask import Flask

app = Flask(__name__)

@app.get('/temperature/<city_name>')
def get_temperature(city_name):
    return f"<h1>{city_name}</h1>"