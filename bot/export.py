from aiogram import Bot, types
from tempfile import NamedTemporaryFile
import pandas as pd
from bot.database.notes_db import get_grouped_notes
from fpdf import FPDF
from aiogram.types import FSInputFile
import os

def prepare_table(grouped_notes: dict):
    max_len = max(len(notes) for notes in grouped_notes.values())
    for tag in grouped_notes:
        grouped_notes[tag] += [''] * (max_len - len(grouped_notes[tag]))

    df = pd.DataFrame(grouped_notes)
    return df

async def export_notes_as_csv(bot: Bot, user_id: int):
    grouped = get_grouped_notes(user_id)

    df = prepare_table(grouped)
    filename = "notes.csv"
    with NamedTemporaryFile(mode='w+', encoding='utf-8', suffix='.csv', delete=False) as tmp:
        df.to_csv(tmp.name, index=False)
        tmp.seek(0)
        await bot.send_document(user_id, types.FSInputFile(tmp.name, filename))

async def export_notes_as_xlsx(bot: Bot, user_id: int):
    grouped = get_grouped_notes(user_id)

    df = prepare_table(grouped)
    filename = "notes.xlsx"
    with NamedTemporaryFile(mode='w+', encoding='utf-8', suffix='.xlsx', delete=False) as tmp:
        df.to_excel(tmp.name, index=False)
        tmp.seek(0)
        await bot.send_document(user_id, types.FSInputFile(tmp.name, filename=filename))

def export_notes_to_pdf(notes: dict, filename: str = "notes.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for tag, tasks in notes.items():
        pdf.set_font("Arial", "B", size=14)
        pdf.cell(200, 10, txt=f"#{tag}", ln=True, align="L")

        pdf.set_font("Arial", size=12)
        for task in tasks:
            pdf.multi_cell(0, 10, txt=f"- {task}", align="L")

        pdf.ln(5)

    pdf.output(filename)

async def export_notes_as_pdf(bot: Bot, user_id: int):
    notes = get_grouped_notes(user_id)
    filename = "notes.pdf"
    export_notes_to_pdf(notes, filename)
    pdf_file = FSInputFile(filename)
    await bot.send_document(user_id, pdf_file)
    os.remove(filename)



def export_notes_to_txt(notes: dict, filename: str = "notes.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for tag, tasks in notes.items():
            file.write(f"#{tag}:\n")
            for task in tasks:
                file.write(f"- {task}\n")
            file.write("\n")


async def export_notes_as_txt(bot: Bot, user_id: int):
    notes = get_grouped_notes(user_id)

    filename = "notes.txt"
    export_notes_to_txt(notes, filename)

    txt_file = FSInputFile(filename)
    await bot.send_document(user_id, txt_file)
    os.remove(filename)


async def export_notes_as_json(bot: Bot, user_id: int):
    grouped = get_grouped_notes(user_id)

    df = prepare_table(grouped)
    filename = "notes.json"
    with NamedTemporaryFile(mode='w+', encoding='utf-8', suffix='.json', delete=False) as tmp:
        df.to_json(tmp.name)
        tmp.seek(0)
        await bot.send_document(user_id, types.FSInputFile(tmp.name, filename=filename))