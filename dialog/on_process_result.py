
from aiogram_dialog import DialogManager


async def on_child_done(start_data, result, manager: DialogManager):
    if not result:
        return
    data = manager.dialog_data.get("options", {})
    _ = manager.middleware_data["i18n"].gettext

    data.update(result)
    manager.dialog_data["options"] = data
