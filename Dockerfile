FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y cron

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

COPY . /code/

# Setup cron schedules from file cron_lines
COPY cron_lines /etc/cron.d/cron_lines
RUN chmod 0644 /etc/cron.d/cron_lines
RUN crontab /etc/cron.d/cron_lines
