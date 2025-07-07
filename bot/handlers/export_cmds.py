from aiogram import Router, types, F, Bot
from aiogram.filters import Command, CommandObject
from bot.database.notes_db import get_all_notes_grouped_by_tag, get_grouped_notes, get_notes_by_tag
from bot.export import export_notes_as_csv, export_notes_as_xlsx, export_notes_as_json, export_notes_as_pdf, export_notes_as_txt
from bot.handlers.keyboard import file_type

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

@export_router.message(Command("export"))
async def cmd_export(message: types.Message, bot: Bot):
    notes = get_grouped_notes(message.from_user.id)
    if not notes:
        await message.answer("📭 You have no notes to export.")
        return
    await message.answer("Choose type of document", reply_markup=file_type)

@export_router.callback_query(F.data == "export_xlsx")
async def export_xlsx(callback: types.CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    await callback.answer("Export..")
    await export_notes_as_xlsx(bot, user_id)

@export_router.callback_query(F.data == "export_csv")
async def export_csv(callback: types.CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    await callback.answer("Export..")
    await export_notes_as_csv(bot, user_id)

@export_router.callback_query(F.data == "export_json")
async def export_json(callback: types.CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    await callback.answer("Export..")
    await export_notes_as_json(bot, user_id)

@export_router.callback_query(F.data == "export_pdf")
async def export_pdf(callback: types.CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    await callback.answer("Export..")
    await export_notes_as_pdf(bot, user_id)

@export_router.callback_query(F.data == "export_txt")
async def export_txt(callback: types.CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    await callback.answer("Export..")
    await export_notes_as_txt(bot, user_id)