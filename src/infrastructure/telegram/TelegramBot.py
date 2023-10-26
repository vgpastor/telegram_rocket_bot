from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from src.application.RocketLaunchBot import RocketLaunchBot
from src.infrastructure.framex.FrameXVideoService import FrameXVideoService

class TelegramBot:
    def __init__(self, token):
        self.app = ApplicationBuilder().token(token).build()
        self.video_service = FrameXVideoService()
        self.bot = RocketLaunchBot(self.app, self.video_service)
        self.app.add_handler(CommandHandler("hello", self.hello))

    async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    async def run(self):
        await self.bot.run()


# if __name__ == "__main__":
#     app = ApplicationBuilder().token("6085702257:AAHfRfXtn4Vaf6sKAm3g02c_vlTRBl7Mvo8").build()
#
#     app.add_handler(CommandHandler("hello", hello))
#     # app.add_handler(CommandHandler("start", start))
#     # app.add_handler(CallbackQueryHandler(button_callback))
#
#     # Luego podrías iniciar y ejecutar el bot así:
#
#     # app_builder = ApplicationBuilder().token("YOUR TOKEN HERE")
#     video_service = FrameXVideoService()
#     bot = RocketLaunchBot(app, video_service)
#     bot.run()
#
#     app.run_polling()
