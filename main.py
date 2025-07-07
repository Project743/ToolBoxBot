import asyncio
import logging
import sys

from config import TOKEN, i18n
from handlers import routers
from dialog import dialogs
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from aiogram.utils.i18n import SimpleI18nMiddleware

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

dp = Dispatcher(storage=MemoryStorage())

dp.update.middleware(SimpleI18nMiddleware(i18n))

# Регистрируем все хендлеры
for router in routers:
    dp.include_router(router)
# Подключаем поддержку диалогов
setup_dialogs(dp)
for dialog in dialogs:
    dp.include_router(dialog)


async def start_bot() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
