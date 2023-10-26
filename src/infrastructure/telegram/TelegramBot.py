from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes


class TelegramBot:
    def __init__(self, token):
        self.app = ApplicationBuilder().token(token).build()
        self.app.add_handler(CommandHandler("hello", self.hello))
        self.app.add_handler(CommandHandler("start", self.hello))

    async def hello(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    def run(self):
        self.app.run_polling()
