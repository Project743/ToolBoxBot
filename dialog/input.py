import re
import phonenumbers

from aiogram_dialog import Window, Dialog, DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message


# ====== Validators ======
EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")


def is_valid_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))


def is_valid_phone(phone: str) -> bool:
    try:
        parsed = phonenumbers.parse(phone, None)
        return phonenumbers.is_valid_number(parsed)
    except phonenumbers.NumberParseException:
        return False


# ====== States ======
class InputSG(StatesGroup):
    input = State()


# ====== Input Handler ======
async def on_input(message: Message, dialog, manager: DialogManager):
    _ = manager.middleware_data["i18n"].gettext
    option = manager.dialog_data.get("option")
    text = (message.text or "").strip()

    if message.content_type != "text":
        await message.answer(_("please_send_text_message"))
        return

    # Option handlers map
    validators = {
        "input_len_pass": validate_password_length,
        "input_email": validate_email,
        "input_phone": validate_phone,
    }

    validator = validators.get(option)
    if validator:
        error_msg = validator(text, _)
        if error_msg:
            await message.answer(error_msg)
            return

    await manager.done({option: text}, show_mode=ShowMode.SEND)


def validate_password_length(text: str, _: callable) -> str | None:
    if not text.isdigit():
        return _("invalid_number")
    if int(text) < 3:
        return _("password_length_too_short")
    return None


def validate_email(text: str, _: callable) -> str | None:
    if not is_valid_email(text):
        return _("no_valid_email")
    return None


def validate_phone(text: str, _: callable) -> str | None:
    if not is_valid_phone(text):
        return _("no_valid_phone")
    return None


# ====== Input Getter ======
async def input_getter(dialog_manager: DialogManager, **kwargs):
    _ = dialog_manager.middleware_data["i18n"].gettext
    dialog_manager.dialog_data.update(dialog_manager.start_data)

    option = dialog_manager.dialog_data.get("option")

    prompts = {
        "input_len_pass": _("input_len_pass"),
        "wifi_ssid": _("input_wifi_ssid"),
        "wifi_password": _("input_wifi_password"),
        "input_text": _("input_text_or_url"),
        "input_name": _("input_name"),
        "input_phone": _("input_phone"),
        "input_email": _("input_email"),
        "input_org": _("input_org"),


    }

    return {
        "input": prompts.get(option, _("input")),
        "back": _("back"),
    }


# ====== Dialog ======
input_dialog = Dialog(
    Window(
        Format("{input}"),
        MessageInput(on_input),
        Button(
            Format("{back}"),
            id="back_btn",
            on_click=lambda c, b, m: m.done(show_mode=ShowMode.SEND),
        ),
        state=InputSG.input,
        getter=input_getter,
    )
)
