## Running App

```sh
docker-compose up
```

To connect to docker environment:

```sh
docker-compose exec admin_api sh
```

To load initial fixture data, after above command from inside the container:
```sh
# python manage.py loaddata fixtures/permissions.json
# python manage.py loaddata fixtures/roles.json
# python manage.py loaddata fixtures/users.json
# python manage.py loaddata fixtures/orders.json
```

To connect to the postgres db running inside the docker:

```sh
docker-compose exec admin_db psql -U root -h localhost -p 5432 django_admin
```

