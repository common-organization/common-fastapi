from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.routers.users.users_controller import router
app = FastAPI(title="common-fastapi")

app.include_router(router)