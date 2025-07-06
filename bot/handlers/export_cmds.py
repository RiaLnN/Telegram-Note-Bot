from aiogram import Router, types, F
from aiogram.filters import Command, CommandObject
from bot.database.notes_db import get_all_notes_grouped_by_tag
from bot.database.notes_db import get_notes_by_tag
export_router = Router()




@export_router.message(Command("view"))
async def view_command(
        message: types.message,
        command: CommandObject
):
    tag = command.args
    if command.args is None:
        grouped_notes = await get_all_notes_grouped_by_tag(message.from_user.id)

        if not grouped_notes:
            await message.answer("📭 You have no saved notes.")
            return

        result = ""
        for tag, notes in grouped_notes.items():
            result += f"📝 #{tag}\n"
            for note in notes:
                result += f"— {note}\n"
            result += "\n"

        await message.answer(result.strip())
    else:

        grouped_notes = await get_notes_by_tag(message.from_user.id, tag)
        if not grouped_notes:
            await message.answer("You have no that tag")

        content = "\n".join([f"—{content}" for _, content in grouped_notes])

        await message.answer(f"📝 #{tag}\n{content}")
