import log
import settings
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

logger = log.setup_logger(__name__)


async def start(update: Update, context: CallbackContext):
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


def run_bot():
    application = ApplicationBuilder().token(settings.BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    logger.info("Starting the bot polling...")
    application.run_polling()
