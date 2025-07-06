from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder




def delete_buttons(contents, tag: str):
    builder = InlineKeyboardBuilder()
    for id, content in contents:
        short = content if len(content) <= 30 else content[:30] + "..."
        builder.add(InlineKeyboardButton(text=f"—{short}", callback_data=f"delete:{id}"))
    builder.add(
        InlineKeyboardButton(text=f"❌ Delete all #{tag}", callback_data=f"delete_tag:{tag}")
    )
    builder.adjust(1)
    return builder.as_markup()
