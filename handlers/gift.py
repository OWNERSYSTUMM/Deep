import asyncio

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from bot import app

@app.on_callback_query(filters.regex("^gift$"))
async def gift_open(client, callback_query):

    msg = callback_query.message

    await msg.edit_text(
        """
🎁 ʟᴇɢᴇɴᴅᴀʀʏ ɢɪғᴛ

👑 +999 ʀᴇsᴘᴇᴄᴛ
🚀 +999 ɢʀᴏᴡᴛʜ
💎 +999 sᴜᴄᴄᴇss
❤️ +∞ ʜᴀᴘᴘɪɴᴇss
"""
    )

    await asyncio.sleep(3)

    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "🎆 Fireworks",
                callback_data="fireworks"
            )
        ]]
    )

    await msg.edit_text(
        "🎁 ɢɪғᴛ ᴏᴘᴇɴᴇᴅ!",
        reply_markup=keyboard
    )
