import validators
from bot import run_bot
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scraper.scraper import scrape


class Data(BaseModel):
    url: str


app = FastAPI()

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

    return {"data": scrape(data.url)}


if __name__ == "__main__":
    run_bot()
