from pyrogram import filters
from pyrogram.types import Message

from meow import app
from meow.core.call import meow 


@app.on_message(filters.video_chat_started, group=20)
@app.on_message(filters.video_chat_ended, group=30)
@app.on_message(filters.left_chat_member)
async def force_stop_stream(_, message: Message):
    try:
        if message.left_chat_member and not message.left_chat_member is None:
            if message.left_chat_member.id == (await get_assistant(message.chat.id)).id:
                return await meow.force_stop_stream(message.chat.id)
        await meow.force_stop_stream(message.chat.id)
    except Exception:
        pass