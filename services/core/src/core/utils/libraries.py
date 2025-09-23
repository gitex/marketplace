from contextlib import contextmanager


@contextmanager
def required_libraries(*libraries):
    """Context manager for imports.

    Usage:
        >>> with required_libraries("django"):
                from django.db import models  # noqa

        >>> with required_libraries("fastapi", "pydantic"):
                from pydantic import BaseModel # noqa
                from fastapi import FastAPI  # noqa
    """
    try:
        yield
    except ImportError as e:
        raise RuntimeError(f"Install libraries: [{','.join(libraries)}]") from e
