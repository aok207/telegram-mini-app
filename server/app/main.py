from bot.app import run_bot
from fastapi import FastAPI
from log import setup_logger

logger = setup_logger(__name__)


app = FastAPI()


@app.get("/api")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    run_bot()
