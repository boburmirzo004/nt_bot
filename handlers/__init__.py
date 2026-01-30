from statistics import median

from aiogram import Router

from handlers import start, chat


def incloud_routers():
    main_router = Router()
    main_router.include_router(start.router)
    main_router.include_router(chat.router)

    return main_router