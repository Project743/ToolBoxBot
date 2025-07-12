from aiogram_dialog import Dialog
from dialog.qr_generate import windows
from dialog import on_process_result
qr_dialog = Dialog(windows.qr_window(), windows.wifi_qr_window(), windows.text_qr_window(), windows.contact_qr_window(), on_process_result=on_process_result.on_child_done)
