from aiogram import Dispatcher

from .start import start_router
from .notes import notes_router
from .export_cmds import export_router
from .misc import misc_router

def register_all_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(misc_router)
    dp.include_router(export_router)
    dp.include_router(notes_router)