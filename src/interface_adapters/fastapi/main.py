from fastapi import FastAPI

from src.interface_adapters.fastapi.routes import api_router


app = FastAPI()


app.include_router(api_router)
