import asyncio

async def type_text(msg, text, delay=0.03):
    current = ""

    for ch in text:
        current += ch

        try:
            await msg.edit_text(current)
        except:
            pass

        await asyncio.sleep(delay)
