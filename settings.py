import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: Final = os.getenv("BOT_TOKEN") or "TOKEN"
BOT_USERNAME = os.getenv("BOT_USERNAME") or "BOT_USERNAME"
