import asyncio
import threading


import pyrogram 
import uvloop
from flask import Flask
from pyrogram import Client, idle
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import (
    BotCommand,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

import config

from ..logging import LOGGER

uvloop.install()

# Flask app initialize
app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is running"


def run():
    app.run(host="0.0.0.0", port=8000, debug=False)


# VIPBot Class
class nobita(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot")
        super().__init__(
            "meow",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = get_me.first_name + " " + (get_me.last_name or "")
        self.mention = get_me.mention

        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="๏ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ๏",
                        url=f"https://t.me/{self.username}?startgroup=true",
                    )
                ]
            ]
        )

        if config.LOG_GROUP_ID:
            try:
                await self.send_message(
                    config.LOG_GROUP_ID,
                 "╔════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪\n║\n║┣⪼🥀𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐚𝐛𝐲🎉\n║\n║┣⪼ {self.name}\n║\n║┣⪼🎈𝐈𝐃:- `{self.id}` \n║\n║┣⪼🎄@{self.username} \n║ \n║┣⪼💖𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠😍\n║\n╚════════════════❍⊱❁",
                    reply_markup=button,
                )
            except pyrogram.errors.ChatWriteForbidden as e:
                LOGGER(__name__).error(f"Bot cannot write to the log group: {e}")
                try:
                    await self.send_message(
                        config.LOG_GROUP_ID,
                        f"╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║┣⪼🥀𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐚𝐛𝐲🎉\n║\n║◈ {self.name}\n║\n║┣⪼🎈𝐈𝐃:- `{self.id}` \n║\n║┣⪼🎄@{self.username} \n║ \n║┣⪼💖𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠😍\n║\n╚══════════════❍⊱❁",
                        reply_markup=button,
                    )
                except Exception as e:
                    LOGGER(__name__).error(f"Failed to send message in log group: {e}")
            except Exception as e:
                LOGGER(__name__).error(
                    f"Unexpected error while sending to log group: {e}"
                )
        else:
            LOGGER(__name__).warning(
                "LOG_GROUP_ID is not set, skipping log group notifications."
            )
        if config.SET_CMDS:
            try:       
                await self.set_bot_commands(
                    commands=[
                        BotCommand("start", "sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ"),
                        BotCommand("play", "sᴏɴɢ ɴᴀᴍᴇ ᴛᴏ ᴘʟᴀʏ "),
                        BotCommand("vplay", "sᴏɴɢ-ᴠɪᴅᴇᴏ ɴᴀᴍᴇ ᴛᴏ ᴘʟᴀʏ ᴛʜᴇ ᴠɪᴅᴇᴏ ɪɴ ᴠᴄ"),
                        BotCommand("cplay", "ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴄʜᴀɴɴᴇʟ"),
                        BotCommand("end", "sᴛᴏᴘ ᴛʜᴇ ᴘʟᴀʏɪɴɢ sᴏɴɢ"),
                        BotCommand("skip", "sᴋɪᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ"),
                    ],
                    scope=    BotCommandScopeAllGroupChats(),
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to set bot commands: {e}")

        if config.LOG_GROUP_ID:
            try:
                chat_member_info = await self.get_chat_member(
                    config.LOG_GROUP_ID, self.id
                )
                if chat_member_info.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error(
                        "Please promote Bot as Admin in Logger Group"
                    )
            except Exception as e:
                LOGGER(__name__).error(f"Error occurred while checking bot status: {e}")

        LOGGER(__name__).info(f"MusicBot Started as {self.name}")


# Define the async boot function
async def anony_boot():
    bot = nobita()
    await bot.start()
    await idle()


if __name__ == "__main__":
    LOGGER(__name__).info("Starting Flask server...")

    # Start Flask server in a new thread
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

    LOGGER(__name__).info("Starting meow...")

    # Run the bot
    asyncio.run(anony_boot())

    LOGGER(__name__).info("Stopping meow...")