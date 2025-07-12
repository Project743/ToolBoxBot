from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_kb(_):
    buttons = [
        KeyboardButton(text=_("pass_generate")),
        KeyboardButton(text=_("qr_generate")),
        KeyboardButton(text=_("suggestion"))
    ]
    return ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)
