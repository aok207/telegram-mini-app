import os
from dotenv import load_dotenv
from typing import Final


load_dotenv()

BOT_TOKEN: Final = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
