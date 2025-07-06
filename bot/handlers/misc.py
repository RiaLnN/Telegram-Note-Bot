from aiogram import Router, types, F
from aiogram.filters import Command, CommandObject

from bot.database.notes_db import delete_all_notes
from bot.database.notes_db import get_notes_by_tag
from bot.database.notes_db import delete_note_by_id
from bot.database.notes_db import delete_tag

from bot.handlers.keyboard import delete_buttons

misc_router = Router()

@misc_router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "<b>🆘 Available Commands:</b>\n\n"
        "/start — Show welcome message\n"
        "/help — Show this help message\n"
        "/view — View all your saved notes\n"
        "/clear — delete all notes"
        "/delete <tag>— Possibility to change tag\n"
        "/export — Export your notes as a file\n\n"
        "📝 Just send any message starting with a tag (e.g., #idea New project) to save it."
    )

@misc_router.message(Command("clear"))
async def clear_command(message: types.Message):
    await delete_all_notes(message.from_user.id)
    await message.answer("🧹 All your notes have been deleted.")

@misc_router.message(Command("delete"))
async def delete_command(message: types.Message, command: CommandObject):
    tag = command.args
    if not tag:
        await message.answer("❗ Write a tag to delete notes from")
        return

    notes = await get_notes_by_tag(message.from_user.id, tag)
    if not notes:
        await message.answer("❌ No notes found for this tag.")
        return

    await message.answer("🗑 Choose a note to delete:", reply_markup=delete_buttons(notes, tag))

@misc_router.callback_query(lambda c: c.data and c.data.startswith("delete:"))
async def delete_note_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    note_id = int(callback.data.split(":")[1])

    await delete_note_by_id(user_id, note_id)

    await callback.answer("✅ Note deleted")
    await callback.message.delete()

@misc_router.callback_query(lambda c: c.data and c.data.startswith("delete_tag:"))
async def delete_tag_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    tag = callback.data.split(":", 1)[1]

    await delete_tag(user_id, tag)


    await callback.answer(f"✅ Deleted tag #{tag}")
    await callback.message.delete()



