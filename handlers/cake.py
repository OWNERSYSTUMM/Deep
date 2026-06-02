import asyncio

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from vikky import app
from config import DEEP_ID

@app.on_callback_query(filters.regex("^cake$"))
async def cake_cut(client, callback_query):

    if callback_query.from_user.id != DEEP_ID:
        await callback_query.answer(
            "🚫 Only Deep Yadav can cut the cake!",
            show_alert=True
        )
        return

    msg = callback_query.message

    progress = [
        "█░░░░░░░░░ 10%",
        "██░░░░░░░░ 20%",
        "███░░░░░░░ 30%",
        "████░░░░░░ 40%",
        "█████░░░░░ 50%",
        "██████░░░░ 60%",
        "███████░░░ 70%",
        "████████░░ 80%",
        "█████████░ 90%",
        "██████████ 100%"
    ]

    for p in progress:
        await msg.edit_text(
            f"🎂 ᴄᴜᴛᴛɪɴɢ ᴄᴀᴋᴇ...\n\n{p}"
        )
        await asyncio.sleep(0.5)

    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "🎁 Open Gift",
                callback_data="gift"
            )
        ]]
    )

    await msg.edit_text(
        "🎂 ᴄᴀᴋᴇ ᴄᴜᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!",
        reply_markup=keyboard
    )
