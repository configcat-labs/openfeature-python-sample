from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import configcatclient
from dotenv import load_dotenv
import os

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize the ConfigCat client
    client = configcatclient.get(os.getenv("CONFIGCAT_SDK_KEY"))
    app.state.client = client
    yield
    # shut down the client
    client.close()


app = FastAPI(lifespan=lifespan)


class Course(BaseModel):
    id: int
    title: str
    author: str
    price: float


courses = [
    Course(id=1, title="Intro to HTML", author="Guy Person", price=49.99),
    Course(id=2, title="Intro to JavaScript", author="Mister Coder", price=59.99),
    Course(id=3, title="Building APIs with Go", author="Sir Programmer", price=60.99),
]


@app.get("/")
def welcome():
    return {"Welcome to courses app"}


@app.get("/courses/")
def get_courses():
    is_get_courses_enabled = app.state.client.get_value('get_courses_enabled', False)
    if is_get_courses_enabled:
        return {"courses": courses}
    else:
        raise HTTPException(status_code=404)
