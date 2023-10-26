from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes


class RocketLaunchBot:
    def __init__(self, app, video_service):
        self.app = app
        self.video_service = video_service

        self.video_name = "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"  # Por ejemplo
        video_info = self.video_service.get_video_info(self.video_name)
        self.left_bound = 0
        self.right_bound = video_info.frames - 1

        self.app.add_handler(CommandHandler("video", self.start_bisection_search))
        self.app.add_handler(CallbackQueryHandler(self.button_callback))

    async def start_bisection_search(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Tomamos el frame del medio para iniciar la búsqueda
        self.current_frame = (self.left_bound + self.right_bound) // 2
        await self.send_video_frame(update.message, context)  # Pasamos update.message aquí

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
        await self.send_video_frame(query.message, context)  # Pasamos query.message aquí

