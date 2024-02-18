FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y libpq-dev gcc && \
    apt-get clean

RUN pip install --upgrade pip

RUN pip install --no-cache-dir poetry

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . .

EXPOSE 80

RUN chmod +x ./start_server.sh

ENTRYPOINT ["./start_server.sh"]
