from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from contextlib import asynccontextmanager
from db import create_tables,delete_tables
from schemas import STaskAdd
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова')
    yield
    print('Выключение')

app = FastAPI(lifespan=lifespan)
 

app.include_router(tasks_router)