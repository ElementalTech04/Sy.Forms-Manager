from fastapi import FastAPI
from routers import contact_controller

app = FastAPI()


app.include_router(contact_controller.router, prefix="/form/contact")

