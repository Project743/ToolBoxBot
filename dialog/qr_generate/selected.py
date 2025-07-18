from aiogram.types import CallbackQuery, InputFile, BufferedInputFile
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from dialog.input import InputSG
from utils.generate_qr import WiFiQRCode, TextQRCode, VCardQRCode


async def on_click_wifi_ssid(c, b, m: DialogManager):
    await m.start(InputSG.input, data={"option": "wifi_ssid"})


async def on_click_wifi_password(c, b, m: DialogManager):
    await m.start(InputSG.input, data={"option": "wifi_password"})

async def on_click_input_text(c, b, m: DialogManager):
    await m.start(InputSG.input, data={"option": "input_text"})

async def on_click_input_name(c, b, m: DialogManager):
    await m.start(InputSG.input, data={"option": "input_name"})

async def on_click_input_phone(c, b, m: DialogManager):
    await m.start(InputSG.input, data={"option": "input_phone"})
async def on_click_input_email(c, b, m: DialogManager):
    await m.start(InputSG.input, data={"option": "input_email"})
async def on_click_input_org(c, b, m: DialogManager):
    await m.start(InputSG.input, data={"option": "input_org"})


async def generate(callback: CallbackQuery, button: Button, manager: DialogManager):
    _ = manager.middleware_data["i18n"].gettext
    data = manager.dialog_data
    qr_type = data.get("qr_type")
    option = data.get("options",{})
    if qr_type == "wifi":
        if option.get("wifi_ssid") is None:
            await callback.message.answer(_("need_input_name_wifi"))
            return
        ssid = option.get("wifi_ssid")
        password = option.get("wifi_password")
        qr = WiFiQRCode(ssid=ssid, password=password)
    elif qr_type == "text":
        text = option.get("input_text")
        qr = TextQRCode(text=text)
    elif qr_type == "vcard":
        if option.get("input_name") is None:
            await callback.message.answer(_("need_input_name_contact"))
            return
        name = option.get("input_name")
        phone = option.get("input_phone")
        email = option.get("input_email")
        org = option.get("input_org")
        qr = VCardQRCode(name=name, phone=phone, email=email, org=org)
    else:
        # можно вернуть ошибку
        return

    qr_file = qr.generate()
    qr_file.seek(0)
    file = BufferedInputFile(qr_file.read(), filename="qr.png")
    await callback.message.answer_document(file)
