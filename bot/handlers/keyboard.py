from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



file_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📄 Excel", callback_data="export_xlsx")],
        [InlineKeyboardButton(text="📊 CSV", callback_data="export_csv")],
        [InlineKeyboardButton(text="🧩 JSON", callback_data="export_json")],
        [InlineKeyboardButton(text="📰 PDF", callback_data="export_pdf")],
        [InlineKeyboardButton(text="📜 TXT", callback_data="export_txt")]
    ]
)
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
