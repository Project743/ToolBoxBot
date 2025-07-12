from aiogram.fsm.state import StatesGroup, State


class QRGenerateSG(StatesGroup):
    main = State()
    wifi_qr = State()
    text_qr = State()
    vcard_qr = State()