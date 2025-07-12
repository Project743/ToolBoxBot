from aiogram import Router
from aiogram.types import ErrorEvent
from aiogram_dialog.api.exceptions import UnknownIntent
import logging
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from keyboards import startkb

error_router = Router()

@error_router.error()
async def error_handler(event: ErrorEvent):
    exception = event.exception
    update = event.update

    # 👉 Попробуем вытащить локаль из сообщения (если вдруг используешь SimpleI18nMiddleware)
    locale = None
    if hasattr(update, "from_user"):
        locale = update.from_user.language_code
    elif hasattr(update, "message") and update.message:
        locale = update.message.from_user.language_code
    elif hasattr(update, "callback_query") and update.callback_query:
        locale = update.callback_query.from_user.language_code

    # Фолбэк переводчика
    def _(text): return text

    if locale:
        # Тут подставь свой способ инициализации I18n
        i18n = I18n(domain="messages", path="locales")
        _ = i18n.gettext

    if isinstance(exception, UnknownIntent):
        logging.info("UnknownIntent обработан.")

        text = _("button_is_outdated")
        reply_markup = startkb.start_kb(_)

        if update.callback_query:
            # Удаляем старое сообщение
            try:
                await update.callback_query.message.delete()
            except Exception as e:
                logging.warning(f"Не удалось удалить сообщение: {e}")

            await update.callback_query.message.answer(text, reply_markup=reply_markup)

        elif update.message:
            await update.message.answer(text, reply_markup=reply_markup)

        return True

    logging.error(f"❌ Неизвестная ошибка: {exception}", exc_info=True)
    return False
