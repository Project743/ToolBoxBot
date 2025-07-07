from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram_dialog import StartMode, DialogManager

from dialog.pass_generate import PassGenSG
from config import i18n

_ = i18n.gettext
__ = i18n.lazy_gettext
router = Router()


@router.message(F.text == __("pass_generate"))
async def generate_password(message: Message, dialog_manager: DialogManager):
    if message.chat.type != "private":
        return
    await message.delete()

    await dialog_manager.start(PassGenSG.main, mode=StartMode.RESET_STACK)
