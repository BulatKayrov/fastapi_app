from fastapi import FastAPI

from api_v1 import api_router

app = FastAPI()
app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', reload=True)
