FROM python:3.8.10

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=4500"]