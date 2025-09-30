from collections.abc import AsyncIterator

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from src.main import app


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://localhost") as client:
            yield client
