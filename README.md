# OpenWeatherAPI

This is a Flask app that consumes OpenWeatherAPI and creates cache in SQLite3.

## How to run

```
$ cp .env.example .env
$ make build
$ make flask
```

Access http://127.0.0.1:4500/temperature/\<city_name\>