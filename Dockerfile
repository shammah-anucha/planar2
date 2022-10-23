# Inspired from: https://www.youtube.com/watch?v=Z8_P5pjmlrg
# Pull base image
FROM python:3.10-slim-buster as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.2.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    # VENV_PATH="/home/shammah/.cache/pypoetry/virtualenvs/planar2-YJ5AWKQv-py3.10"
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Builder Image
FROM python-base as builder-base

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev 

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
# RUN pip install poetry

WORKDIR $PYSETUP_PATH

COPY pyproject.toml poetry.lock ./

RUN poetry install

# RUN poetry shell

# Production Image
FROM python-base as production

COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

COPY ./backend /backend/

ENV POSTGRES_PASSWORD=not-happening-again

# CMD ["poetry", "./planar/backend/app/app/main.py"]

CMD ["uvicorn", "backend.app.app.main:app", "--host", "0.0.0.0", "--port", "80"]
