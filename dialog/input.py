from aiogram_dialog import Window, Dialog, DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format
from aiogram.fsm.state import State, StatesGroup


class InputSG(StatesGroup):
    input = State()


async def on_input(message, dialog, manager: DialogManager):
    _ = manager.middleware_data["i18n"].gettext
    option = manager.dialog_data.get("option")
    if message.content_type != "text":
        await message.answer(_("please_send_text_message"))
        return

    text = message.text or ""

    if option == "input_len_pass":
        if not text.isdigit():
            await message.answer(_("invalid_number"))
            return

        length = int(text)
        if length < 3:
            await message.answer(_("password_length_too_short"))
            return

    await manager.done({option: text}, show_mode=ShowMode.SEND)


async def input_getter(dialog_manager: DialogManager, **kwargs):
    _ = dialog_manager.middleware_data["i18n"].gettext
    dialog_manager.dialog_data.update(dialog_manager.start_data)
    option = dialog_manager.dialog_data.get("option")
    return {
        "input": _("input"),
        "back": _("back"),
    }


input_dialog = Dialog(
    Window(
        Format("{input}"),
        MessageInput(on_input),
        Button(Format("{back}"), id="add_text", on_click=lambda c, b, m: m.done(show_mode=ShowMode.SEND)),
        state=InputSG.input,
        getter=input_getter
    )
)
