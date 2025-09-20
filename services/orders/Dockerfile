ARG PYTHON_VERSION=3.12 
FROM python:${PYTHON_VERSION}-slim AS builder 

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG POETRY_VERSION=2.2.0 
ENV POETRY_HOME=/opt/poetry \ 
    POETRY_NO_INTERACTION=1 \ 
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    PATH="/opt/poetry/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential git \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python - \
    && ln -s ${POETRY_HOME}/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* ./ 

ARG INSTALL_DEV="false"
RUN if [ "$INSTALL_DEV" = "true" ]; then \
    poetry install --no-root --with dev ; \
    else \
    poetry install --no-root;  \
    fi

COPY . . 

RUN if [ "$INSTALL_DEV" = "true" ]; then \
    poetry install --with dev ; \
    else \
    poetry install; \
    fi

# Runtime
FROM python:${PYTHON_VERSION}-slim AS runtime 

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

RUN useradd -m appuser
WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app 

RUN chown -R appuser:appuser /app
USER appuser 



