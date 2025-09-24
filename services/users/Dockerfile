ARG PYTHON_VERSION=3.12

# ----------- Stage Build -------------
FROM python:${PYTHON_VERSION}-slim AS builder 

# uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_NO_CACHE=1

# uv output level: info, debug, trace
ARG UV_LOG_LEVEL=info
ENV RUST_LOG=$UV_LOG_LEVEL

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Required for 'core' installation
ARG INTERNAL_PYPI_INDEX_URL \
    INTERNAL_PYPI_INDEX_USER \ 
    INTERNAL_PYPI_INDEX_PASSWORD 

ENV UV_DEFAULT_INDEX="internal=${INTERNAL_PYPI_INDEX_URL}"  \
    UV_INDEX_INTERNAL_USERNAME=${INTERNAL_PYPI_INDEX_USER} \
    UV_INDEX_INTERNAL_PASSWORD=${INTERNAL_PYPI_INDEX_PASSWORD}

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project 

ARG INSTALL_DEV=false
RUN if [ "$INSTALL_DEV" = "true" ]; then \
    uv sync --locked --no-install-project; \
    else \ 
    uv sync --locked --no-dev --no-install-project; \
    fi 

COPY . . 

RUN --mount=type=cache,target=/root/.cache/uv \
    if [ "$INSTALL_DEV" = "true" ]; then \
    uv sync --locked; \
    else \
    uv sync --locked --no-dev; \
    fi

# Runtime
FROM python:${PYTHON_VERSION}-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

RUN apt-get update && \
    apt-get upgrade --assume-yes && \
    # cURL necessary to "healthcheck"
    apt-get install curl --assume-yes && \
    rm --recursive --force /var/lib/apt/lists/*

# Add for security reasons
# Need to replace because of https://pythonspeed.com/articles/root-capabilities-docker-security
RUN useradd -m app 
WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app /app 

ENV VIRTUAL_ENV=/app/.venv \
    PATH="$VIRTUAL_ENV/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Add for security reasons
RUN chown -R app:app /app
USER app 
