### Quick start

0. Install [Docker](https://www.docker.com/)

1. Migrate db

```docker-compose run web python /code/manage.py migrate --noinput```
2. Create admin user

```docker-compose run web python /code/manage.py createsuperuser```

3. Run server

```docker-compose up -d --build```

### Postman

- [collection](https://www.getpostman.com/collections/bd9dff6e04b792d09ec7)

### Demo

- http://165.22.95.119:8000/
