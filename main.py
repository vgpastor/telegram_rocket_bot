#!/usr/bin/.env python3

from os import environ, path
from sys import path as py_path
from sys import stderr
import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from src.application.RocketLaunchBot import RocketLaunchBot
from src.infrastructure.framex.FrameXVideoService import FrameXVideoService

from src.application.HelloBotCommand import HelloBotCommand
ROOT = path.dirname(__file__)

import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    app = ApplicationBuilder().token("6085702257:AAHfRfXtn4Vaf6sKAm3g02c_vlTRBl7Mvo8").build()

    # app.add_handler(CommandHandler("hello", hello))
    # app.add_handler(CommandHandler("start", start))
    # app.add_handler(CallbackQueryHandler(button_callback))

    # Luego podrías iniciar y ejecutar el bot así:

    # app_builder = ApplicationBuilder().token("YOUR TOKEN HERE")
    video_service = FrameXVideoService()
    bot = RocketLaunchBot(app, video_service)

    helloCommand = HelloBotCommand(app)

    app.run_polling()
