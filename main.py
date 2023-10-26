#!/usr/bin/.env python3

from os import path
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from src.application.RocketLaunchBot import RocketLaunchBot
from src.infrastructure.framex.FrameXVideoService import FrameXVideoService

from src.application.HelloBotCommand import HelloBotCommand

from src.infrastructure.telegram.TelegramBot import TelegramBot

ROOT = path.dirname(__file__)

import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    # bot = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    #
    # helloCommand = HelloBotCommand(app)
    #

    bot = TelegramBot(os.getenv("TELEGRAM_BOT_TOKEN"))

    video_service = FrameXVideoService()
    rocket_launcher = RocketLaunchBot(bot.app, video_service)

    # bot.run_polling()
    bot.run()


