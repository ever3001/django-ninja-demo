# django-ninja-demo

A very simple (just [two endpoints](src/users/api/views.py)) django-ninja API.

Features
- Poetry based
- type hinted
  - run `bash bin/types.sh`
- tested
  - run `bash bin/tests.sh`
- with [custom user model](src/users/models.py)
  - [Using a custom user model when starting a project](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
  - https://testdriven.io/blog/django-custom-user-model/
- JWT auth support
  - with [dev user auto login](src/users/middleware.py) middleware
  - including [test client](src/users/tests/api/utils.py)
- easy local setup
  - run `cp .env.example .env` to duplicate the env file and you are good to
    go [for local development]
  - [faker based] [fixture data](src/users/fixtures/users.json) included
  - [setup_dev_env](src/users/management/commands/setup_dev_env.py) command
    - plus other [helper commands](src/users/management/commands)
- served with [uvicorn/gunicorn](bin/server.sh)
- dockerized
    - run `docker compose up -V`
