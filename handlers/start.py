from aiogram import Router
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.i18n import SimpleI18nMiddleware, I18n
from aiogram_dialog.api.exceptions import UnknownIntent
from keyboards.startkb import start_kb
from config import i18n

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, i18n: I18n):
    _ = i18n.gettext  # Локализованный _
    await message.answer(
        _("welcome_message"),
        reply_markup=start_kb(_)  # Передаём локализованный _
    )
