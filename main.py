from fastapi import FastAPI
from routes.main import router

app = FastAPI(title="Structural Change API")

app.include_router(router, prefix="/api")