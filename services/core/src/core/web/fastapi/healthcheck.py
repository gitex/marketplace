"""
Используется для быстрой интеграции healthcheck в сервисы с fastapi.

Использование:
    app = FastAPI()
    app.include_router(healthcheck_router)
"""

from fastapi import APIRouter, status
from pydantic import BaseModel

healthcheck_router = APIRouter()


class HealthCheckResponse(BaseModel):
    status: str = "OK"


@healthcheck_router.get(
    "/health",
    tags=["healthcheck"],
    summary="Проверка работоспособности сервера",
    response_description="Возвращает HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheckResponse,
)
def get_health() -> HealthCheckResponse:
    return HealthCheckResponse(status="OK")
