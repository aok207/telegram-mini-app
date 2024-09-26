from typing import Literal

import validators
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scraper.scraper import crawl_website


class Data(BaseModel):
    url: str
    depth: Literal[1, 2, 3]


app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.post("/api/submit")
async def submit_form(data: Data, response: Response):
    if not validators.url(data.url):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Please enter a valid url!"}

    if data.depth not in [1, 2, 3]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Depth should be 1, 2, or 3"}

    return {"data": crawl_website(data.url, data.depth if data.depth else 1)}
