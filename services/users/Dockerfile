ARG PYTHON_VERSION=3.12
ARG SOURCE_DIR="app"

# Builder
FROM python:${PYTHON_VERSION}-slim AS builder 

ARG SOURCE_DIR

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG POETRY_VERSION=2.2.0 
ENV POETRY_HOME=/opt/poetry \ 
    POETRY_NO_INTERACTION=1 \ 
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    PATH="/opt/poetry/bin:$PATH"

# Add for security reasons
# RUN adduser --home /${SOURCE_DIR} app 
# USER app

RUN apt-get update && \
    apt-get upgrade --assume-yes && \
    apt-get install -y --no-install-recommends \
    curl build-essential git \
    && rm --recursive --force /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python - \
    && ln -s ${POETRY_HOME}/bin/poetry /usr/local/bin/poetry


WORKDIR /${SOURCE_DIR}

# Required for 'core' installation
ARG INTERNAL_PYPI_SOURCE_NAME="internal"
ARG INTERNAL_PYPI_SOURCE_URL
ARG INTERNAL_PYPI_SOURCE_USER 
ARG INTERNAL_PYPI_SOURCE_PASSWORD 

ENV POETRY_REPOSITORIES_${INTERNAL_PYPI_SOURCE_NAME}_URL=${INTERNAL_PYPI_SOURCE_URL}
ENV POETRY_HTTP_BASIC_${INTERNAL_PYPI_SOURCE_NAME}_USERNAME=${INTERNAL_PYPI_SOURCE_USER}
ENV POETRY_HTTP_BASIC_${INTERNAL_PYPI_SOURCE_NAME}_PASSWORD=${INTERNAL_PYPI_SOURCE_PASSWORD}

# Install packages
COPY pyproject.toml poetry.lock ./ 

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# RUN poetry config repositories.${INTERNAL_PYPI_SOURCE_NAME} ${INTERNAL_PYPI_SOURCE_URL}

ARG INSTALL_DEV=false 
RUN if [ "$INSTALL_DEV" = "true" ]; then \
    poetry install --no-root --with dev ; \
    else \
    poetry install --no-root; \
    fi

COPY . . 

RUN if [ "$INSTALL_DEV" = "true" ]; then \
    poetry install --with dev ; \
    else \
    poetry install; \
    fi

# Runtime
FROM python:${PYTHON_VERSION}-slim AS runtime 

ARG SOURCE_DIR

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/${SOURCE_DIR}/.venv/bin:$PATH"

RUN apt-get update && \
    apt-get upgrade --assume-yes && \
    # cURL necessary to "healthcheck"
    apt-get install curl --assume-yes && \
    rm --recursive --force /var/lib/apt/lists/*

# Add for security reasons
# Need to replace because of https://pythonspeed.com/articles/root-capabilities-docker-security
RUN useradd -m app 
WORKDIR /${SOURCE_DIR}

COPY --from=builder /${SOURCE_DIR}/.venv /${SOURCE_DIR}/.venv
COPY --from=builder /${SOURCE_DIR} /${SOURCE_DIR} 

# Add for security reasons
RUN chown -R app:app /${SOURCE_DIR}
USER app 
