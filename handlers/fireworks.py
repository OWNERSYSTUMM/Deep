import asyncio
from pyrogram import filters

from bot import app

@app.on_callback_query(filters.regex("^fireworks$"))
async def fireworks(client, callback_query):

    msg = callback_query.message

    frames = [
        "✨🎆✨",
        "🎆✨🎆",
        "✨🎇✨",
        "🎇✨🎇",
        "💥🎆💥"
    ]

    for frame in frames:
        await msg.edit_text(frame)
        await asyncio.sleep(1)

    await msg.type_text(
        """
👑 ᴅᴇᴇᴘ ʏᴀᴅᴀᴠ 👑

🎂 ʜᴀᴘᴘʏ ʙɪʀᴛʜᴅᴀʏ 🎂

🚀 ʟᴇᴠᴇʟ ɪɴᴄʀᴇᴀsᴇᴅ
💎 ᴀᴄʜɪᴇᴠᴇᴍᴇɴᴛ ᴜɴʟᴏᴄᴋᴇᴅ
👑 ᴋɪɴɢ sᴛᴀᴛᴜs

❤️ sᴛᴀʏ ʟᴇɢᴇɴᴅᴀʀʏ
"""
    )
