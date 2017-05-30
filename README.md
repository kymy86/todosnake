ToDoSnake
====

Simple ToDo list application with Python Flask back-end and XXXX front-end.

1. Rename env_example in .env
2. run docker-compose up


## Db Migration

`docker-compose run --rm backend python manage.py db init`

`docker-compose run --rm backend python manage.py db upgrade`

`docker-compose run --rm backend python manage.py db migrate`

`docker-compose run --rm backend python manage.py db downgrade`

## Test

`docker-compose run --rm backend python -m unittest`

## Database connect

`docker exec -it todosnake_postgresdb_1 psql dbname dbuser`