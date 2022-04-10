# OpenWeatherAPI

This is a Flask app that consumes OpenWeatherAPI and creates cache in SQLite3.

## Requirements
- Docker
- docker-compose
- make

## How to run

I created a makefile to make easier run the docker commands. This script contains the following commands:

| makefile command | command that will be run           | what it does                                 |
|------------------|------------------------------------|----------------------------------------------|
| make flask       | flask run                          | run flask locally                            |
| make build       | docker build                       | builds the docker image                      |
| make run         | docker-compose up                  | run the docker image                         |
| make update      | docker-compose up --force-recreate | updates the image with changes in Dockerfile |
| make stop        | docker-compose down                | stop running the docker image                |
| bash             | docker run -it bash                | access console in the running image          |


You can start the project on docker running the following commands in your terminal:
```
$ git clone git@github.com:Camilotk/OpenWeatherAPI.git
$ cd OpenWeatherAPI/
$ cp .env.example .env
$ make build
$ make run
```

Access http://127.0.0.1:4500/temperature/\<city_name\>

An example of returned JSON from this endpoint is:
```JSON
{
  "avg": 298.78,
  "country": "BR",
  "max": 299.93,
  "min": 297.64,
  "name": "Guará"
}
```

## Endpoints

The base URL is one of:
- http://127.0.0.1:4500/ if you are running from docker with command `make run`
- http://127.0.0.1:5000/ if you are running from local enviroment with command `make flask`

The API has the following endpoints:
| endpoint                        | http method | JSON data                                                                                                                                                                              |
|---------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /temperature/\<**city_name**\>      | GET         | Get the current temperature for the specified city_name , either from cache or from the Open Weather API, if not already cached (and still valid).  Data mappings are described below. |
| /temperature/\<**city_name**\>?max=\<**max_number**\> | GET         | Get the cached temperatures for up to the latest max_number queried cities (through the above endpoint)   

No authentication is required on any endpoint.

### Check the API

This API is deployed on Heroku https://openapiweatherdev.herokuapp.com/ (note that root '/' is empty), you can use curl to access it:

```
$ curl https://openapiweatherdev.herokuapp.com/temperature/farroupilha -H "Accept: application/json"
```
It returns:
```JSON
{"avg":289.5,"country":"BR","max":290.63,"min":288.38,"name":"Farroupilha"}
```
