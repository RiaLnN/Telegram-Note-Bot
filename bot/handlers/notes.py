from aiogram import Router, types
import re
from bot.database.notes_db import save_note

notes_router = Router()

@notes_router.message()
async def handle_note(message: types.Message):
    text = message.text.strip()
    match = re.match(r"#(\w+)\s+(.+)", text)

    if not match:
        await message.answer("❌ Please start your message with a tag (e.g., #idea Build a bot)")
        return

    tag, content = match.groups()

    await save_note(user_id=message.from_user.id, tag=tag.lower(), content=content)
    await message.answer(f"✅ Saved note under tag #{tag}")
