from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from openfeature import api
from configcat_openfeature_provider import ConfigCatProvider
from dotenv import load_dotenv
import os

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize ConfigCat client
    cc_provider = ConfigCatProvider(os.getenv("CONFIGCAT_SDK_KEY"))
    # enable the ConfigCat provider
    api.set_provider(cc_provider)
    client = api.get_client()
    app.state.client = client
    yield
    # clean up all providers
    api.shutdown()


app = FastAPI(lifespan=lifespan)


class Course(BaseModel):
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
    is_get_courses_enabled = app.state.client.get_boolean_value('get_courses_enabled', False)
    if is_get_courses_enabled:
        return {"courses": courses}
    else:
        raise HTTPException(status_code=404)
