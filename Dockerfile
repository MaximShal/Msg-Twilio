FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get install -y netcat-openbsd

RUN mkdir /app
WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip3 install --upgrade pip wheel setuptools
RUN pip3 install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY ./ ./
COPY startup.sh ./

CMD ["bash", "./startup.sh"]