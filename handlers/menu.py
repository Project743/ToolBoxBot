from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram_dialog import StartMode, DialogManager

from dialog.pass_generate import PassGenSG
from dialog.qr_generate.states import QRGenerateSG
from    dialog.suggestion import SuggestionSG
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



@router.message(F.text == __("qr_generate"))
async def generate_qr(message: Message, dialog_manager: DialogManager):
    if message.chat.type != "private":
        return
    await message.delete()

    await dialog_manager.start(QRGenerateSG.main, mode=StartMode.RESET_STACK)





@router.message(F.text == __("suggestion"))
async def suggestion(message: Message, dialog_manager: DialogManager):
    if message.chat.type != "private":
        return
    await message.delete()

    await dialog_manager.start(SuggestionSG.main, mode=StartMode.RESET_STACK)
