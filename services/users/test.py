from contextlib import contextmanager


@contextmanager
def required_libraries(*libraries):
    try:
        yield
    except ImportError as e:
        raise RuntimeError(f"Install libraries: [{','.join(libraries)}]") from e


with required_libraries("django"):
    from flask import db  # noqa
