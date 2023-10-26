from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes, Application

from src.domain.AbstractVideoService import AbstractVideoService


class RocketLaunchBot:
    def __init__(self, app: Application, video_service: AbstractVideoService):
        self.app = app
        self.video_service = video_service

        self.video_name = "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"
        self.video_info = self.video_service.get_video_info(self.video_name)

        self.resetData()

        self.app.add_handler(CommandHandler("video", self.start_bisection_search))
        self.app.add_handler(CallbackQueryHandler(self.button_callback))

    def resetData(self):
        self.left_bound = 0
        self.right_bound = self.video_info.frames - 1

    async def start_bisection_search(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.resetData()
        self.current_frame = (self.left_bound + self.right_bound) // 2
        await self.send_video_frame(update.message, context)

    async def send_video_frame(self, message, context: ContextTypes.DEFAULT_TYPE) -> None:
        frame = self.video_service.get_frame(self.video_name, self.current_frame)
        keyboard = [
            [InlineKeyboardButton("Sí", callback_data='yes'),
             InlineKeyboardButton("No", callback_data='no')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await message.reply_photo(photo=frame.url, reply_markup=reply_markup, caption="¿Ha despegado el cohete?")

    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        query = update.callback_query
        if query.data == 'yes':
            self.right_bound = self.current_frame
        else:
            self.left_bound = self.current_frame + 1

        if self.left_bound >= self.right_bound:
            await query.edit_message_text(text=f"¡El cohete despegó en el frame {self.right_bound}!")
            return

        self.current_frame = (self.left_bound + self.right_bound) // 2
        await self.send_video_frame(query.message, context)

