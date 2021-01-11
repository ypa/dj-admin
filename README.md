## Running App

```sh
docker-compose up
```

To connect to docker environment:

```sh
docker-compose exec admin_api sh
```

To connect to the postgres db running inside the docker:

```sh
psql -U root -h localhost -p 55432 django_admin
```
