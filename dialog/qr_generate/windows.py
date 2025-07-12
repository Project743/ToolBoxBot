from aiogram_dialog import Window, ShowMode
from aiogram_dialog.widgets.kbd import SwitchTo, Button
from aiogram_dialog.widgets.text import Format

from dialog import on_process_result
from dialog.qr_generate.states import QRGenerateSG
from dialog.qr_generate import getters, selected



def qr_window():
    return Window(
        Format("{select_qr}"),
        SwitchTo(Format("{wifi_qr}"), id="wifi_qr", state=QRGenerateSG.wifi_qr),
        SwitchTo(Format("{contact_qr}"), id="contact_qr", state=QRGenerateSG.vcard_qr),
        SwitchTo(Format("{text_qr}"), id="text_qr", state=QRGenerateSG.text_qr),
        Button(Format("{back}"), id="add_text", on_click=lambda c, b, m: m.done(show_mode=ShowMode.SEND)),
        getter=getters.qr_getter,
        state=QRGenerateSG.main,
    )



def wifi_qr_window():
    return Window(
        Format("{input_wifi_for_qr}"),
        Button(Format("{wifi_ssid}"), id="wifi_ssid", on_click=selected.on_click_wifi_ssid),
        Button(Format("{wifi_password}"), id="wifi_password", on_click=selected.on_click_wifi_password),
        Button(Format("{generate}"), id="generate", on_click=selected.generate),
        SwitchTo(Format("{back}"), id="add_text", state=QRGenerateSG.main),
        getter=getters.wifi_qr_getter,
        state=QRGenerateSG.wifi_qr,

    )

def text_qr_window():
    return Window(
        Format("{input_text_for_qr}"),
        Button(Format("{input_text}"), id="input_text", on_click=selected.on_click_input_text),
        Button(Format("{generate}"), id="generate", on_click=selected.generate),
        SwitchTo(Format("{back}"), id="add_text", state=QRGenerateSG.main),
        getter=getters.text_qr_getter,
        state=QRGenerateSG.text_qr,

    )

def contact_qr_window():
    return Window(
        Format("{input_contact_for_qr}"),
        Button(Format("{input_name}"), id="input_name", on_click=selected.on_click_input_name),
        Button(Format("{input_phone}"), id="input_phone", on_click=selected.on_click_input_phone),
        Button(Format("{input_email}"), id="input_email", on_click=selected.on_click_input_email),
        Button(Format("{input_org}"), id="input_org", on_click=selected.on_click_input_org),
        Button(Format("{generate}"), id="generate", on_click=selected.generate),
        SwitchTo(Format("{back}"), id="add_text", state=QRGenerateSG.main),
        getter=getters.contact_qr_getter,
        state=QRGenerateSG.vcard_qr,

    )
