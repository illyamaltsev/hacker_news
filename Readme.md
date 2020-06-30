### Quick start

1. Install [Docker](https://www.docker.com/)

2. Migrate db

    ```docker-compose run web python /code/manage.py migrate --noinput```

3. Create admin user

    ```docker-compose run web python /code/manage.py createsuperuser```

4. Run server

    ```docker-compose up -d --build```
    
    *Or use ```docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build``` in production*

### Postman

- [collection](https://www.getpostman.com/collections/bd9dff6e04b792d09ec7)

### Demo

- http://165.22.95.119:8000/
