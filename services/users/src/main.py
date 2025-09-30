from contextlib import asynccontextmanager

from core.web.fastapi.healthcheck import healthcheck_router
from fastapi import FastAPI

from src.config import settings
from src.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    debug=settings.debug,
    title=settings.name,
    lifespan=lifespan,
)

app.include_router(healthcheck_router)
app.include_router(users_router)
# app.include_router(addresses_router)

#
# @app.middleware("http")
# async def add_process_time(request: Request, call_next):
#     start_time = time.perf_counter()
#     response = await call_next(request)
#     process_time = time.perf_counter() - start_time
#     response.headers["X-Process-Time"] = process_time
#     return response
