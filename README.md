# 🗂️ AutoNotes — Telegram Note Bot with Tags

A simple and efficient Telegram bot that helps you save and organize notes using tags. Powered by `aiogram v3` and `SQLite`.

---

## 🚀 Features

- Add notes using `#tag` syntax  
  → Example: `#study Learn SQL syntax`
- View all notes by tag: `/view study`
- Delete individual notes using inline buttons
- Delete all notes under a tag
- Clean architecture and modular handlers
- SQLite-based local database
- `.env` configuration support
- (Coming soon) Export notes to `.txt` or `.csv`

---

## 💬 Basic Commands

| Command                 | Description                     |
|-------------------------|---------------------------------|
| `/start`                | Welcome message                 |
| `/help`                 | Bot usage instructions          |
| `/view (optional)<tag>` | View all notes or under a tag   |
| `/delete <tag>`         | Show inline buttons to delete   |
| `/clear`                | Clear all user notes |

---

## 🧪 Example Usage

Simply message the bot:

#life Plan my week

#study Learn about aiogram 3

Then use `/view life` or `/delete study` to manage them.

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/RiaLnN/Telegram-Note-Bot.git
cd auto-notes
2. Install requirements
pip install -r requirements.txt
3. Add environment variables
Create a .env file in the root:

BOT_TOKEN=your_telegram_bot_token_here

📌 Tech Stack
Python 3.10+

aiogram 3

SQLite3

Python-dotenv

📦 To Do
 -Export notes to .txt or .csv

 -User-friendly tag browsing

 -Admin features

 -Cloud DB support (e.g., Supabase)