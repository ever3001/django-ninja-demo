FROM python:3.11-slim as poetry

ENV POETRY_HOME=/opt/poetry
ENV POETRY_VERSION=1.3.2

RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -

# --------------------------------------------------------------------------- #
FROM python:3.11-slim as dependencies

COPY --from=poetry /opt/poetry /opt/poetry

WORKDIR /app
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:/app/.venv/bin:$PATH"

# `psycopg2` build dependencies.
# In production it is advised to use the package built from sources.
RUN \
  apt -y update && \
  apt -y install gcc libpq-dev && \
  apt clean && \
  rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

# --------------------------------------------------------------------------- #
FROM python:3.11-slim as development

COPY --from=poetry /opt/poetry /opt/poetry
COPY --from=dependencies /app /app

WORKDIR /app
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN \
  apt -y update && \
  apt -y install git entr libpq-dev && \
  apt clean && \
  rm -rf /var/lib/apt/lists/*

RUN poetry install --no-root
