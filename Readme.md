### RUN 

- Migrate db

```docker-compose run web python /code/manage.py migrate --noinput```
- Create admin user

```docker-compose run web python /code/manage.py createsuperuser```

- Run server

```docker-compose up -d --build```