from fastapi import FastAPI
from controller import contact_controller

app = FastAPI()


app.include_router(contact_controller.router, prefix="/contactForms")

