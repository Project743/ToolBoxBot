from aiogram_dialog.api.exceptions import NoContextError
from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram_dialog import DialogManager

class DialogResetMiddleware(BaseMiddleware):
    def __init__(self, reset_commands: list[str] = None):
        self.reset_commands = reset_commands or ["/start"]

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        dialog_manager: DialogManager = data.get("dialog_manager")
        if dialog_manager and event.text and event.text.strip().lower() in self.reset_commands:
            try:
                await dialog_manager.reset_stack()
            except NoContextError:
                pass

        return await handler(event, data)
