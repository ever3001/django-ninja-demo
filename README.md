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

## How to Use

To set up and start using the application, follow these steps. Make sure Docker is installed on your system before you begin.

1. Prepare Environment Variables:
    
    Before starting the application, you need to set up your environment variables. A template file named `.env.example` is provided in the repository. Copy this file to create your own `.env` file, which you can then edit according to your needs.

    ```bash
    cp .env.example .env
    ```

    Important: The `.env` file contains sensitive information and should not be committed to the repository. This file is ignored by the `.gitignore` file to prevent it from being accidentally shared.
    
2. Start the Application:
    
    Launch the application using Docker Compose. This command will build, (re)create, start, and attach to containers for a service.

    ```bash
    docker compose up
    ```

3. Collect Static Files:
    
    With the application running, your next step is to collect static files. These are essential for the proper display and functionality of your application. Execute the following command:

    ```bash
    docker exec django-ninja-demo-app-1 poetry run python src/manage.py collectstatic
    ```

    Confirm the operation when prompted to ensure all static files are properly gathered.
    
4. Setup Development Environment:
    
    Finalize your setup by configuring the development environment, which includes importing sample data and applying necessary configurations with the following command:

    ```bash
    docker exec django-ninja-demo-app-1 poetry run python src/manage.py setup_dev_env
    ```


Following these steps will get your Django-Ninja demo application up and running, with all the necessary configurations and environment set up.