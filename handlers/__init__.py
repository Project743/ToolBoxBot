from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.errors import error_router
from handlers.donate import router as d_router



# Список всех маршрутов
routers = [
    start_router,
    menu_router,
    error_router,
    d_router,
]