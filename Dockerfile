# Define base image for the container
FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "5000", "--log-level", "info", "--reload"]