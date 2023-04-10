#!/bin/bash
set -e

# https://www.uvicorn.org/deployment/
#   Run `uvicorn --reload` from the command line for local development.
#   Run `gunicorn -k uvicorn.workers.UvicornWorker` for production.
#   The `--reload` and `--workers` arguments are mutually exclusive.
if [ "${ENVIRONMENT}" == "development" ]; then
    exec uvicorn myapp.asgi:application \
        --host 0.0.0.0 \
        --port 8000 \
        --app-dir "$(pwd)"/src \
        --reload \
        --reload-include "*.html"
else
    exec gunicorn myapp.asgi:application \
        --name myapp-server \
        --bind 0.0.0.0:8000 \
        --worker-class uvicorn.workers.UvicornWorker \
        --workers "${SERVER_WORKERS}" \
        --timeout "${SERVER_TIMEOUT}" \
        --max-requests "${SERVER_MAX_REQUESTS}" \
        --chdir "$(pwd)"/src
fi
