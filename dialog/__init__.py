from dialog.pass_generate import gen_pass_dialog
from dialog.input import input_dialog
from dialog.qr_generate import qr_dialog
from dialog.suggestion import suggestion_dialog


# Список всех маршрутов
dialogs = [
    gen_pass_dialog,
    input_dialog,
    qr_dialog,
    suggestion_dialog,

]