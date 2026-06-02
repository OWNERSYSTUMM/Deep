from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "birthday_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

import handlers.birthday
import handlers.cake
import handlers.gift
import handlers.fireworks

print("🎂 Birthday Bot Started...")
app.run()
