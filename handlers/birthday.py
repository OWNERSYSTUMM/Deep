from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from bot import app

@app.on_message(filters.command("birthday"))
async def birthday_start(client, message):

    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "🎂 Cut Cake",
                callback_data="cake"
            )
        ]]
    )

    await message.type_text(
        """
🎬 ʙɪʀᴛʜᴅᴀʏ ᴇᴠᴇɴᴛ

👑 ᴅᴇᴇᴘ ʏᴀᴅᴀᴠ

👇 ᴘʀᴇss ᴛᴏ sᴛᴀʀᴛ
""",
        reply_markup=keyboard
    )
