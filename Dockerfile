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

# Copy hello-cron file to the cron.d directory
COPY cron_lines /etc/cron.d/cron_lines

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron_lines

# Apply cron job
RUN crontab /etc/cron.d/cron_lines

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
