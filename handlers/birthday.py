print("birthday.py loaded")
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from bot import app

@app.on_message(filters.command("birthday"))
async def birthday_start(client, message):
    print("Birthday command received")
    await message.reply_text("Bot Working")

    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "🎂 Cut Cake",
                callback_data="cake"
            )
        ]]
    )

    await message.reply_text(
        """
🎬 ʙɪʀᴛʜᴅᴀʏ ᴇᴠᴇɴᴛ

👑 ᴅᴇᴇᴘ ʏᴀᴅᴀᴠ

👇 ᴘʀᴇss ᴛᴏ sᴛᴀʀᴛ
""",
        reply_markup=keyboard
    )
