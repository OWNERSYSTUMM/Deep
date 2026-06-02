import asyncio

async def type_text(msg, text, delay=0.04):
    current = ""

    for char in text:
        current += char

        try:
            await msg.edit_text(current)
        except:
            pass

        await asyncio.sleep(delay)
