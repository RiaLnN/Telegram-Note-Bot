import sqlite3
from bot.config import load_config

config = load_config()

async def create_db():
    conn = sqlite3.connect(config.db_path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            tag TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

async def save_note(user_id: int, tag: str, content: str):
    conn = sqlite3.connect(config.db_path)
    c = conn.cursor()
    c.execute("INSERT INTO notes (user_id, tag, content) VALUES (?, ?, ?)", (user_id, tag, content))
    conn.commit()
    conn.close()

async def get_notes_by_tag(user_id: int, tag: str):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM notes WHERE user_id = ? AND tag = ?", (user_id, tag.lower()))
    notes = cursor.fetchall()
    conn.close()
    return notes

async def get_all_notes_grouped_by_tag(user_id: int):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT tag, content FROM notes WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()

    grouped = {}
    for tag, content in rows:
        if tag not in grouped:
            grouped[tag] = []
        grouped[tag].append(content)
    return grouped

async def delete_all_notes(user_id: int):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

async def delete_note_by_id(user_id: int, note_id: int):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE user_id = ? AND id = ?", (user_id, note_id))
    conn.commit()
    conn.close()

async def delete_tag(user_id: int, tag: str):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE user_id = ? AND tag = ?", (user_id, tag))
    conn.commit()
    conn.close()