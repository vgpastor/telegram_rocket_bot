from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes


class HelloBotCommand:
    def __init__(self, app):
        self.app = app
        self.app.add_handler(CommandHandler("hello", self.hello))

    async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')
