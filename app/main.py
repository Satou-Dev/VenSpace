import fastapi
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import time

app = FastAPI()
templates = Jinja2Templates("templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def homepage(req: Request):
    return templates.TemplateResponse("homepage.html", {"request": req})
