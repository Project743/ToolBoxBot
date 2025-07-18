from aiogram_dialog import Window, Dialog, DialogManager, ShowMode
from aiogram_dialog.widgets.text import Format
from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog.widgets.kbd import Button, Multiselect
from utils.generate_password import PasswordGenerator
from aiogram.types import CallbackQuery
from keyboards.startkb import start_kb
from dialog.input import InputSG
from dialog import on_process_result
from typing import Any
import html





class PassGenSG(StatesGroup):
    main = State()


def options_buttons():
    return Multiselect(
        checked_text=Format("✅ {item[1]}"),
        unchecked_text=Format("▫ {item[1]}"),
        id="selected_options",
        item_id_getter=lambda x: str(x[0]),  # ID канала
        items="options",  # Используем список из getter
    )


async def generate_selection(callback: CallbackQuery, button: Button, manager: DialogManager):
    _ = manager.middleware_data["i18n"].gettext
    selected_options = manager.find("selected_options").get_checked()
    input_len = int(manager.dialog_data["options"]["input_len_pass"])

    use_digits = "use_digits" in selected_options
    use_symbols = "use_symbols" in selected_options

    gen = PasswordGenerator(length=input_len, use_digits=use_digits, use_symbols=use_symbols)
    password = gen.generate()
    safe_password = html.escape(password)
    await callback.message.answer(f"{_("your_password")} <code>{safe_password}</code>", parse_mode="HTML", reply_markup=start_kb(_))


async def pass_getter(dialog_manager: DialogManager, **kwargs):
    _ = dialog_manager.middleware_data["i18n"].gettext
    options = [{"name": _("use_digits"), "id": "use_digits"}, {"name": _("use_symbols"), "id": "use_symbols"}]
    pass_options = [(option["id"], option["name"]) for option in options]
    return {
        "input_len_pass": f"{_("input_len_pass")} / {int(dialog_manager.dialog_data["options"]["input_len_pass"])}",
        "generate": _("generate"),
        "select_option": _("select_option"),
        "options": pass_options,
        "back": _("back")
    }


async def on_click_input(c, b, m: DialogManager):
    await m.start(InputSG.input, data={"option": "input_len_pass"})


async def on_start(start_data: Any, manager: DialogManager):
    options = manager.dialog_data.setdefault("options", {})
    options["input_len_pass"] = 12


gen_pass_dialog = Dialog(
    Window(
        Format("{select_option}"),
        Button(Format("{input_len_pass}"), id="input_len_pass", on_click=on_click_input),
        options_buttons(),  # Тут кнопки с каналами (Radio или Multiselect)
        Button(Format("{generate}"), id="generate", on_click=generate_selection),
        Button(Format("{back}"), id="add_text", on_click=lambda c, b, m: m.done(show_mode=ShowMode.SEND)),
        getter=pass_getter,
        state=PassGenSG.main,
    ),
    on_start=on_start,
    on_process_result=on_process_result.on_child_done
)
