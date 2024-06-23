from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from api_v1 import api_router
from config import settings

app = FastAPI()
app.include_router(api_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.Redis.from_url(settings.redis_url, encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis=redis), prefix='cache')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', reload=True)
