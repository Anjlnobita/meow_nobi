from telegraph import upload_file
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from meow import app

# Command handler for the "tgm" or "telegraph" command
@app.on_message(filters.command(["tgm", "telegraph"]))
async def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        try:
            # Inform user about the process
            i = await message.reply("𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺...")
            # Download the file (this is the media file from the reply)
            path = await reply.download()
            # Upload the file to Telegraph
            url = upload_file(path)
            # Edit the message to show the generated link
            await i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ https://telegra.ph/{url[0]}')
        except Exception as e:
            # Handle errors and inform the user
            await message.reply(f"Error occurred while processing: {str(e)}")
    else:
        # If the message is not a reply to a media message
        await message.reply("Please reply to a media message to create a Telegraph link.")

# Command handler for the "graph" or "grf" command
@app.on_message(filters.command(["graph", "grf"]))
async def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        try:
            # Inform user about the process
            i = await message.reply("𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺...")
            # Download the file (this is the media file from the reply)
            path = await reply.download()
            # Upload the file to Graph.org
            url = upload_file(path)
            # Edit the message to show the generated link
            await i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ https://graph.org/{url[0]}')
        except Exception as e:
            # Handle errors and inform the user
            await message.reply(f"Error occurred while processing: {str(e)}")
    else:
        # If the message is not a reply to a media message
        await message.reply("Please reply to a media message to create a Graph link.")