from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram_dialog import Window, ShowMode, DialogManager, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format
from dialog import on_process_result
from config import ADMIN_ID


class SuggestionSG(StatesGroup):
    main = State()


async def suggestion_getter(dialog_manager: DialogManager, **kwargs):
    _ = dialog_manager.middleware_data["i18n"].gettext


    return {
        "input_message": _("input_message"),
        "back": _("back")
    }

async def on_input(message: Message, dialog, manager: DialogManager):
    _ = manager.middleware_data["i18n"].gettext
    text = (message.text or "").strip()

    await message.forward(chat_id=ADMIN_ID)

    await message.answer(_("offer_sent"))

    # отправляем уведомление о успешной отправке предложения
    await manager.done( show_mode=ShowMode.SEND)

suggestion_dialog = Dialog(
    Window(Format("{input_message}"),
        MessageInput(on_input),
        Button(Format("{back}"), id="add_text", on_click=lambda c, b, m: m.done(show_mode=ShowMode.SEND)),
        getter=suggestion_getter,
        state=SuggestionSG.main,
    ),
    on_process_result=on_process_result.on_child_done
)