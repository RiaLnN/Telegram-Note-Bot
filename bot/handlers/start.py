from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import  hbold

start_router = Router()
# Start command
@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Hello, {hbold(user.full_name)}!\n\n"
        f"I'm your 📔 personal Telegram notebook.\n"
        f"Just send me a message starting with a tag (e.g., #study Learn Aiogram), and I’ll save it for you."
    )