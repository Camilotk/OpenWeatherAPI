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

```
$ cp .env.example .env
$ make build
$ make flask
```

Access http://127.0.0.1:4500/temperature/\<city_name\>