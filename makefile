flask:
	@flask run

build:
	@docker build -t openweatherapi_flask .

run:
	@docker-compose up -d

update:
	@docker-compose up --force-recreate --build -d

stop:
	@docker-compose down

test:
	pytest -v -s

bash:
	@docker run -it openweatherapi_api bash