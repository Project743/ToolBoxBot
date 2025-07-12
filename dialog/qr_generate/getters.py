from aiogram_dialog import DialogManager


async def qr_getter(dialog_manager: DialogManager, **kwargs):
    _ = dialog_manager.middleware_data["i18n"].gettext
    print(dialog_manager.dialog_data)

    return {
        "select_qr": _("select_qr"),
        "wifi_qr": _("wifi_qr"),
        "contact_qr": _("contact_qr"),
        "text_qr": _("text_qr"),
        "back": _("back")
    }


async def wifi_qr_getter(dialog_manager: DialogManager, **kwargs):
    _ = dialog_manager.middleware_data["i18n"].gettext
    dialog_manager.dialog_data.update({"qr_type": "wifi"})

    return {
        "input_wifi_for_qr": _("input_wifi_for_qr"),
        "wifi_ssid": _("wifi_ssid"),
        "wifi_password": _("wifi_password"),
        "generate": _("generate"),
        "back": _("back")
    }

async def text_qr_getter(dialog_manager: DialogManager, **kwargs):
    _ = dialog_manager.middleware_data["i18n"].gettext
    dialog_manager.dialog_data.update({"qr_type": "text"})

    return {
        "input_text_for_qr": _("input_text_for_qr"),
        "input_text": _("input_text"),
        "generate": _("generate"),
        "back": _("back")
    }
async def contact_qr_getter(dialog_manager: DialogManager, **kwargs):
    _ = dialog_manager.middleware_data["i18n"].gettext
    dialog_manager.dialog_data.update({"qr_type": "vcard"})

    return {
        "input_contact_for_qr": _("input_contact_for_qr"),
        "input_name": _("input_name"),
        "input_email": _("input_email"),
        "input_phone": _("input_phone"),
        "input_org": _("input_org"),
        "generate": _("generate"),
        "back": _("back")
    }
