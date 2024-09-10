from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import log
import settings

logger = log.setup_logger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat or not update.message:
        return

    kb = [
        [
            InlineKeyboardButton(
                "Launch App",
                web_app=WebAppInfo("https://content-crawl.vercel.app/"),
            )
        ]
    ]

    await update.message.reply_text(
        "🚀 Fetch and save the main content from any URL. Click the button below to get started!",
        reply_markup=InlineKeyboardMarkup(kb),
    )


def run():
    logger.info(f"The bot is running at t.me/{settings.BOT_USERNAME}...")
    application = ApplicationBuilder().token(settings.BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()
