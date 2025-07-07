import os

from aiogram.utils.i18n import I18n
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")  # Юзернейм бота (без @)

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в .env!")
if not BOT_USERNAME:
    raise ValueError("❌ BOT_USERNAME не найден в .env!")

# Путь к папке с переводами
i18n = I18n(path="locales", default_locale="en", domain="messages")